
import qualified Data.Set as S
import Data.List (foldl', partition)
import Control.Arrow ((&&&))

solve = (finish &&& finish2) . go . map words . lines
  where
    finish = sum . map S.size . filter (S.member 0)
    finish2 = length
    go = foldl' (flip process) []
    process (f:_:ts) ss = let from = read f :: Int
                              tos = map read ts
                          in foldl' process1 ss (zip (repeat from) tos)
    process1 ss (f,t) = let (ins,outs) = partition (\s ->  S.member f s || S.member t s) (ensure f . ensure t $ ss)
                        in foldl' S.union S.empty ins:outs
    ensure f ss = let ss' = filter (S.member f) ss
                  in if length ss' >= 1
                     then ss
                     else (S.singleton f : ss)

main = interact (show . solve . init)
