

import qualified Data.Map.Strict as M
import Data.Char
import Debug.Trace

get :: String -> M.Map Char Int -> Int
get x m | isAlpha (head x) = M.findWithDefault 0 (head x) m
        | otherwise        = read x

run :: [String] -> M.Map Char Int -> (Int, Maybe Int) -> Int -> (M.Map Char Int, (Int, Maybe Int), Int)
run ["set",[x],y] m freq ip = let y' = get y m
                              in (M.insert x y' m, freq, ip+1)
run ["sub",x,y] m freq ip = let y' = get y m
                                x' = get x m
                            in (M.insert (head x) (x'-y') m, freq, ip+1)
run ["mul",x,y] m (f,freq) ip = let y' = get y m
                                    x' = get x m
                                in (M.insert (head x) (x'*y') m, (f+1,freq), ip+1)
run ["jnz",x,y] m freq ip = let x' = get x m
                                y' = get y m
                            in (m, freq, if x' /= 0 then ip+y' else ip+1)

solve :: String -> Int
solve = go (M.fromList [('a',1)] :: M.Map Char Int) (0,Nothing) 0 . map words . lines
  where
    go m freq ip is = let i = is !! ip
                          (m', freq', ip') = run i m freq ip
                      in trace ("executing " ++ show i ++ " and " ++ show freq' ++ " h " ++ show (M.lookup 'c' m')) $ go m' freq' ip' is

main = interact (show . solve . init)
