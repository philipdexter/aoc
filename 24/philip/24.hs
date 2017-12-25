
import Data.Char
import Data.Ord
import Data.List
import Data.Maybe

component :: String -> (Int,Int)
component s = let (a,s') = span isDigit s
                  b = takeWhile isDigit (drop 1 s')
              in (read a, read b)

match n (a,b) | n == a    = Just (a,b)
              | n == b    = Just (b,a)
              | otherwise = Nothing

re :: (Int,Int) -> [(Int,Int)] -> [(Int,Int)]
re _ [] = []
re (a,b) ((x,y):xs) | (a,b) == (x,y) || (b,a) == (x,y) = re (a,b) xs
                    | otherwise                        = (x,y):re (a,b) xs

combinations n xs = let ms = catMaybes (map (match n) xs)
                    in case ms of
                         [] -> [[(0,0)]]
                         _ -> concatMap (\m@(a,b) -> map ((a,b):) (combinations b (re m xs))) ms

solve = go . map component . lines
  where
    go = map (sum . map (\(a,b) -> a+b)) . sortBy (comparing length)  . combinations 0

main = interact (show . solve . init)
