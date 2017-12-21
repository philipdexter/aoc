

import Data.Function
import Data.Foldable
import Data.List
import Data.Ord
import Control.DeepSeq

step ((p1,p2,p3),(v1,v2,v3),(a1,a2,a3)) = let (v1',v2',v3') = (v1+a1,v2+a2,v3+a3)
                                          in ((p1+v1',p2+v2',p3+v3'),(v1',v2',v3'),(a1,a2,a3))

parse line = let [p1,p2,p3,v1,v2,v3,a1,a2,a3] = map read line :: [Double]
             in ((p1,p2,p3),(v1,v2,v3),(a1,a2,a3))

solve = take 3 . sortBy (comparing snd) . zip [0..] . map (abs . calculate . parse . words) . lines
  where
    calculate ((p1,p2,p3),(v1,v2,v3),(a1,a2,a3)) = sqrt (sq a1 + sq a2 + sq a3)
    sq = (^2)

solve2 = length . go 10000 . map (parse . words) . lines
  where
    go i a = foldl' (\a _ -> map head . filter ((==1) . length) . groupBy (\x y -> fst' x == fst' y) . sortBy (comparing fst') . map step $ deepseq a a) a [0..i]
    fst' (x,_,_) = x

main = interact ( show . solve2 . init )
