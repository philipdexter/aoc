{-# LANGUAGE TupleSections #-}

import Control.Arrow

solve :: [[String]] -> Int
solve = sum . map (uncurry (flip subtract)) . map ( maximum &&& minimum ) . map (map read)

solve2 :: [[String]] -> Int
solve2 = sum . map sum . map (map abs) . map (map (uncurry mydiv)) . map (filter (uncurry yes)) . map takes2 . map (map (read :: String -> Int))
  where yes a b = mod a b == 0 || mod b a == 0
        mydiv a b | a > b     = a `div` b
                  | otherwise = b `div` a

takes2 :: [Int] -> [(Int,Int)]
takes2 [] = []
takes2 (x:xs) = map (x,) xs ++ takes2 xs

main :: IO ()
main = getContents >>= pure . map words . lines >>= pure . solve2 >>= print
