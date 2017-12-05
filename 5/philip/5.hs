
{-# LANGUAGE BangPatterns #-}

import qualified Data.Array as A

load :: String -> A.Array Integer Integer
load input = let input' = map read (lines input)
                 len = fromIntegral (length input')
             in A.listArray (0,len-1) input'

solve :: String -> String
solve input = show $ go 0 0 (load input)
  where
    go :: Integer -> Integer -> A.Array Integer Integer -> Integer
    go steps idx arr | idx < 0 || idx > snd (A.bounds arr) = steps
                     | otherwise                           = go (steps+1) ((A.!) arr idx + idx) (update idx arr)
    update idx arr = (A.//) arr [(idx, (A.!) arr idx + 1)]

main = interact (solve . init)
