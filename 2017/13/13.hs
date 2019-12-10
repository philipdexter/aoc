
import Control.Arrow ((&&&))


solve = (go &&& go2) . map (map read . words) . lines
  where
    go = sum . map (process 0)
    go2 i = until (\x -> 0 == sum (map (process x) i)) (+1) 0
    process o [x,y] | mod (o+x) (2*(y-1)) == 0 = x*y -- +1 for part 2
                    | otherwise            = 0

main = interact (show . solve . init)
