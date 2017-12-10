
import qualified Data.Map as M
import Data.Maybe
import Data.List
import Data.Bits
import Text.Printf
import Data.Char

input = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]

position x = x `mod` 256
get k m = fromJust (M.lookup k m)

solve = go (M.fromList (zip [0..255] [0..255])) 0 0 input
  where go m p ss (l:ls) = let positions = map position [p..p+l-1]
                               vals = map (flip get m) positions
                               newVals = reverse vals
                               newMap = foldl' (flip (uncurry M.insert)) m (zip positions newVals)
                        in go newMap (p+l+ss) (ss+1) ls
        go m _ _ [] = m

chunksOf n [] = []
chunksOf n xs = take n xs : chunksOf n (drop n xs)

toend = [17, 31, 73, 47, 23]
input2 = map ord "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243" ++ toend

solve2 = let (m, _, _) = a
             list = M.assocs m :: [(Int, Int)]
             chunks = chunksOf 16 (map snd list)
             xored = map (foldl1' xor) chunks
             hex = map (printf "%02x") xored :: [String]
         in concat hex
  where a = foldl' (\(m, p, ss) _ -> go m p ss input2) (M.fromList (zip [0..255] [0..255]), 0, 0) [0..63]
        go m p ss (l:ls) = let positions = map position [p..p+l-1]
                               vals = map (flip get m) positions
                               newVals = reverse vals
                               newMap = foldl' (flip (uncurry M.insert)) m (zip positions newVals)
                        in go newMap (p+l+ss) (ss+1) ls
        go m p ss [] = (m, p, ss)


main = print solve
