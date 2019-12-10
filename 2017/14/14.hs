
import qualified Data.Map as M
import Data.Maybe
import Data.List
import Data.Bits
import Text.Printf
import Data.Char
import qualified Data.Set as S

position x = x `mod` 256
get k m = fromJust (M.lookup k m)

chunksOf n [] = []
chunksOf n xs = take n xs : chunksOf n (drop n xs)

solve i = let (m, _, _) = a
              list = M.assocs m :: [(Int, Int)]
              chunks = chunksOf 16 (map snd list)
              xored = map (foldl1' xor) chunks
              hex = map (printf "%08b") xored :: [String]
          in concat hex
  where a = foldl' (\(m, p, ss) _ -> go m p ss i) (M.fromList (zip [0..255] [0..255]), 0, 0) [0..63]
        go m p ss (l:ls) = let positions = map position [p..p+l-1]
                               vals = map (flip get m) positions
                               newVals = reverse vals
                               newMap = foldl' (flip (uncurry M.insert)) m (zip positions newVals)
                        in go newMap (p+l+ss) (ss+1) ls
        go m p ss [] = (m, p, ss)

toend = [17, 31, 73, 47, 23]
input = "stpzcrnm"
main = let bs = map (\i -> solve (map ord (input ++ "-" ++ show i) ++ toend)) [0..127]
       in print (sum (map (length . (filter (=='1'))) bs))

stree :: [(Int,Int)] -> [S.Set Int]
stree = go
  where
    go = foldl' (flip process) []
    process (f, t) ss = let from = f :: Int
                            tos = [t]
                          in foldl' process1 ss (zip (repeat from) tos)
    process1 ss (f,t) = let (ins,outs) = partition (\s ->  S.member f s || S.member t s) (ensure f . ensure t $ ss)
                        in foldl' S.union S.empty ins:outs
    ensure f ss = let ss' = filter (S.member f) ss
                  in if length ss' >= 1
                     then ss
                     else (S.singleton f : ss)

mkedges = go 0 []
  where
    go :: Int -> [Int] -> [[Int]] -> [(Int,Int)]
    go o prevRow (row:rows) = let curOnes = map snd (filter ((==1) . fst) (zip row [o..]))
                                  curEdges = map (\(_,i) -> (i, i+1)) (filter (\((a,b),_) -> a == 1 && b == 1) (zip (zip row (tail row)) [o..]))
                                  fromAbove = map (\i -> (i,i-128)) (filter (\i -> i-128 `elem` prevRow) curOnes)
                                  alone = zip curOnes curOnes
                              in  curEdges ++
                                  fromAbove ++
                                  alone ++
                                  go (o+128) curOnes rows
    go _ _ [] = []

getfrom1 = map (\i -> map (\i -> ord i - ord '0') (solve (map ord (input ++ "-" ++ show i) ++ toend))) [0..127]

main2 = let s = stree (mkedges (getfrom1)) in length s
