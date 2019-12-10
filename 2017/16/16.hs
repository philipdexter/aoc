import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Data.Ord

solve = go
  where
    go l [] = l
    go l ('s':xs) = let (n,xs') = ((16 - ) . read *** drop 1) . span isDigit $ xs
                        l' = drop n l ++ take n l
                      in go l' xs'
    go l ('x':xs) = let (num,xs') = (read *** drop 1) . span isDigit $ xs
                        (denom,xs'') = (read *** drop 1) . span isDigit $ xs'
                        l' = let (x,y) = (min num denom, max num denom)
                                 (s,e:r) = splitAt x l
                                 (s',e':r') = splitAt (y-x-1) r
                             in s ++ [e'] ++ s' ++ [e] ++ r'
                    in go l' xs''
    go l ('p':xs) = let (num,xs') = (fromJust . flip elemIndex l *** drop 1) . fromJust . uncons $ xs
                        (denom,xs'') = (fromJust . flip elemIndex l *** drop 1) . fromJust . uncons $ xs'
                        l' = let (x,y) = (min num denom, max num denom)
                                 (s,e:r) = splitAt x l
                                 (s',e':r') = splitAt (y-x-1) r
                             in s ++ [e'] ++ s' ++ [e] ++ r'
                    in go l' xs''

solve2 i = foldl' (\(x,a,m) _ -> let a' = solve a i
                                 in case find ((==a').snd) m of
                                      Just (x',a') -> error (show (find ((==(1000000001 `rem` (x+1))).fst) m))
                                      Nothing -> (x+1,a',(x,a'):m))
           (0,['a'..'p'],[]) [0..1000000000]

main = interact (show . (solve ['a'..'p'] &&& solve2) . init)
