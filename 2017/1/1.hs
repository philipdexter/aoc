
import Data.Char (digitToInt)

solve :: String -> String
solve s = let s' = map (digitToInt) s
          in show $ go (head s') s' 0
  where
    go fst (x:y:xs) sum | x == y    = go fst (y:xs) (sum + x)
                        | otherwise = go fst (y:xs) sum
    go fst [x]      sum | x == fst  = sum + x
                        | otherwise = sum

solve2 :: String -> String
solve2 s = let s' = map (digitToInt) s
  in show $ sum $ zipWith (\x y -> if x == y then x else 0) s' (rotate (size `div` 2) s')
  where
    size = length s
    rotate n l = drop n l ++ take n l

main = interact (solve2 . init)
