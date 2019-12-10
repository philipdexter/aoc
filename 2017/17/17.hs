
import Data.List
import Debug.Trace
import Control.Arrow


insertAt 0 x' xs = x':xs
insertAt n x' (x:xs) = x:insertAt (n-1) x' xs

solve i = finish $ foldl' go ([0], 1, 0) [1..2017]
  where
    finish (xs,_,_) = case elemIndex 2017 xs of
                        Just x -> xs !! (x+1)
    go (xs, l, p) x = let p' = (p + i) `mod` l + 1
                      in (insertAt p' x xs, l+1, p')

solve2 i = finish $ foldl' go ([0], 1, 0) [1..50000000]
  where
    finish (xs,_,_) = case elemIndex 0 xs of
                        Just x -> xs !! (x+1)
    go (xs, l, p) x = let p' = (p + i) `mod` l + 1
                      in if p' <= 3 then (insertAt p' x xs, l+1, p') else (xs, l+1, p')





input = 359

main = print ((solve&&&solve2) input)
