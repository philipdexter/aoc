

import qualified Data.Map.Strict as M
import Data.Char

run ["set",[x],[y]] m freq ip | isAlpha y = let y' = M.findWithDefault 0 y m
                                            in (M.insert x y' m, freq, ip)

solve :: String -> Int
solve = go (M.empty :: M.Map Char Int) 0 0 . map words . lines
  where
    go m freq ip is = let i = is !! ip
                          (m', freq', ip') = run i m freq ip
                      in go m' freq' ip' is

main = interact (show . solve . init)
