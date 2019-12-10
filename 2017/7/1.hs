
import Control.Arrow
import qualified Data.Map.Strict as M
import Data.List (foldl', nub)

data Entry = Entry { name :: String, weight :: Int, to :: [String] } deriving Show

readEntry :: String -> Entry
readEntry s = let name:weight:rest = words s
                  weight' = read . tail . init $ weight
                  to = case rest of
                         [] -> []
                         "->":to -> map (filter (/= ',')) to
              in Entry name weight' to

buildMap :: [Entry] -> M.Map String [String]
buildMap = foldl' insert M.empty
  where insert map entry@(Entry name _ to) =
          foldl' (\m k -> M.insertWith (++) k [name] m) map to

buildMap2 :: [Entry] -> M.Map String Entry
buildMap2 = foldl' insert M.empty
  where insert map entry@(Entry name _ _) = M.insert name entry map

readEntries = lines >>> map readEntry >>> buildMap2

findBottom :: M.Map String [String] -> String
findBottom = M.assocs >>> map (snd >>> head) &&& map fst >>> finish >>> head
  where finish (xs, ys) = filter (\x -> not (elem x ys)) xs

findBalance m = finish "svugo" $ mutate m
  where mutate = M.map costOf
        costOf :: Entry -> [(String, Int, Bool)]
        costOf = to >>> map (\x -> (x, (flip findOrError m >>> weight) x, (flip findOrError m >>> to >>> null) x))
        findOrError x m = case M.lookup x m of
          Nothing -> error x
          Just x -> x
        finish :: String -> M.Map String [(String, Int, Bool)] -> Int
        finish x m =
          let to = findOrError x m
          in if and (map thrd to)
             then (if (not . ((==1) . length) . nub . map sd) to then (if null to then 0 else error (show (to))) else sum (map sd to))
             else let to' = zip (map sd to) (map (\x -> sd x + finish (fs x) m) to)
                  in error (show x ++ " --- " ++ show to ++ "  ---- " ++ show to')
        thrd (_,_,a) = a
        sd (_,a,_) = a
        fs (a,_,_) = a

solve = readEntries >>> findBalance >>> show

main = interact solve
