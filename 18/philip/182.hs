

import qualified Data.Map.Strict as M
import Data.Char
import Control.DeepSeq

type Program = (M.Map Char Int, (Int, Maybe Int), Int, [Int])

get :: String -> M.Map Char Int -> Int
get x m | isAlpha (head x) = M.findWithDefault 0 (head x) m
        | otherwise        = read x

run :: [String] -> Program -> (Program, Maybe Int)
run ["set",[x],y] (m, freq, ip, mb) = let y' = get y m
                                      in ((M.insert x y' m, freq, ip+1, mb), Nothing)
-- run ["snd",y] (m, (_,freq), ip, mb) = let y' = get y m
--                                       in ((m, (y',freq), ip+1, mb), Nothing)
run ["add",x,y] (m, freq, ip, mb) = let y' = get y m
                                        x' = get x m
                                    in ((M.insert (head x) (x'+y') m, freq, ip+1, mb), Nothing)
run ["mul",x,y] (m, freq, ip, mb) = let y' = get y m
                                        x' = get x m
                                    in ((M.insert (head x) (x'*y') m, freq, ip+1, mb), Nothing)
run ["mod",x,y] (m, freq, ip, mb) = let y' = get y m
                                        x' = get x m
                                    in ((M.insert (head x) (x'`mod`y') m, freq, ip+1, mb), Nothing)
-- run ["rcv",x] (m, (f,freq), ip, mb) = let x' = get x m
--                                       in ((m, (f, if x' /= 0 then error (show f) -- Just f
--                                                else freq), ip+1, mb), Nothing)
run ["jgz",x,y] (m, freq, ip, mb) = let x' = get x m
                                        y' = get y m
                                    in ((m, freq, if x' > 0 then ip+y' else ip+1, mb), Nothing)
run ["rcv",[x]] (m, freq, ip, mb) = case mb of
                                      [] -> ((m, freq, ip, []), Nothing)
                                      (i:mb) -> ((M.insert x i m, freq, ip+1, mb), Nothing)
run ["snd",x] (m, freq, ip, mb) = let x' = get x m
                                  in ((m, freq, ip+1, mb), Just x')

solve :: String -> Int
solve = go 0 pr1 pr2 . map words . lines
  where
    pr1 = (M.fromList [('p',0)], (0,Nothing), 0, [])
    pr2 = (M.fromList [('p',1)], (0,Nothing), 0, [])
    go p1sc pr1@(m1, freq1, ip1, mb1) pr2@(m2, freq2, ip2, mb2) is =
      let a@((m1', freq1', ip1', mb1'), o1) = run (is !! ip1) pr1
          b@((m2', freq2', ip2', mb2'), o2) = run (is !! ip2) pr2
      in if ip1 == ip1' && ip2 == ip2' then p1sc
         else deepseq a (deepseq b $
                         go (if head (is !! ip2) == "snd" then p1sc + 1 else p1sc)
                         (m1', freq1', ip1', case o2 of Nothing -> mb1' ; Just x -> mb1' ++ [x])
                         (m2', freq2', ip2', case o1 of Nothing -> mb2' ; Just x -> mb2' ++ [x]) is)

main = interact (show . solve . init)
