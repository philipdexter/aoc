
import Data.Bits
import Debug.Trace
import Data.Int
import Text.Printf
import Control.Arrow

(>-) f g = (>>>) f g
(&) x f = f x
infixr 0 &

first16 :: Int -> [Bool]
first16 = testBit >- flip map [0..15]

fromBool True = 1
fromBool False = 0

factors = (16807, 48271)
divisor = 2147483647

pairs = 40000000
pairs2 = 5000000

start = (277, 349) :: (Int,Int)

solve = go 0
  where
    go i (a,b) | i < pairs = let (x',y') = (a*fst factors `rem` divisor, b*snd factors `rem` divisor)
                                 score = if first16 x' == first16 y' then 1 else 0
                             in score + go (i+1) (x',y')
               | otherwise = 0

solve2 = go 0
  where
    go i (a,b) | i < pairs2 = let (a',b') = (genfst a, gensnd b)
                                  genfst x = let try = x*fst factors `rem` divisor
                                             in if try `rem` 4 == 0 then try else genfst try
                                  gensnd y = let try = y*snd factors `rem` divisor
                                             in if try `rem` 8 == 0 then try else gensnd try
                                  score = first16 a' == first16 b' & fromBool
                              in score + go (i+1) (a',b')
               | otherwise = 0

main = start & (solve &&& solve2) >- print
