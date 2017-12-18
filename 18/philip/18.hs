

import qualified Data.Map.Strict as M
import Data.Char
import Debug.Trace

get :: String -> M.Map Char Int -> Int
get x m | isAlpha (head x) = M.findWithDefault 0 (head x) m
        | otherwise        = read x

run :: [String] -> M.Map Char Int -> (Int, Maybe Int) -> Int -> (M.Map Char Int, (Int, Maybe Int), Int)
run ["set",[x],y] m freq ip = let y' = get y m
                              in (M.insert x y' m, freq, ip+1)
run ["snd",y] m (_,freq) ip = let y' = get y m
                              in (m, (y',freq), ip+1)
run ["add",x,y] m freq ip = let y' = get y m
                                x' = get x m
                            in (M.insert (head x) (x'+y') m, freq, ip+1)
run ["mul",x,y] m freq ip = let y' = get y m
                                x' = get x m
                            in (M.insert (head x) (x'*y') m, freq, ip+1)
run ["mod",x,y] m freq ip = let y' = get y m
                                x' = get x m
                            in (M.insert (head x) (x'`mod`y') m, freq, ip+1)
run ["rcv",x] m (f,freq) ip = let x' = trace "hi" $ get x m
                              in (m, (f, if x' /= 0 then error (show f) -- Just f
                                       else freq), ip+1)
run ["jgz",x,y] m freq ip = let x' = get x m
                                y' = get y m
                            in (m, freq, if x' > 0 then ip+y' else ip+1)

solve :: String -> Int
solve = go (M.empty :: M.Map Char Int) (0,Nothing) 0 . map words . lines
  where
    go m freq ip is = let i = is !! ip
                          (m', freq', ip') = run i m freq ip
                      in trace ("executing " ++ show i ++ " and " ++ show freq') $ go m' freq' ip' is

main = interact (show . solve . init)
