
import Data.List
import Data.Maybe

type Program = [String]

variations rule = rotations rule ++ (rotations (flipped rule))
  where
    flipped = map reverse
    rotations xs = let rotate = reverse . transpose
                   in xs : snd (foldl' (\(x,a) _ -> let x' = rotate x
                                                    in (x',x':a)) (xs,[]) [0..2])

spliton _ [] = []
spliton c xs = let (a,b) = span (/=c) xs
               in a : spliton c (drop 1 b)

chunksof _ [] = []
chunksof n xs = take n xs : chunksof n (drop n xs)

parse = map (sides . words) . lines
  where
    sides [before,"=>",after] = (rule before, rule after)
    rule a = let splits = spliton '/' a
                 size = length splits
             in (size, splits)

splitup n xs = let a = map (chunksof n) xs
                   b = chunksof n a
               in map (map (chunksof n) . foldl1' (zipWith (++))) b

matches prog ((_,before),(_,after)) | any (==prog) before = Just after
                                    | otherwise           = Nothing

stepprogram :: Program -> [[Program]]
stepprogram a = let size = length a
                    splitby = if size `rem` 2 == 0 then 2 else 3
                    parts = splitup splitby a
                in parts

unwrap :: [[Program]] -> Program
unwrap = concat . map (foldl1' (zipWith (++)))

step prog book = let progparts = stepprogram prog
                 in unwrap $ map (map (\p -> (head . catMaybes) (map (matches p) book))) progparts

solve = length . filter (=='#') . concat . go [".#.","..#","###"] . map (\((i,before), after) -> ((i,variations before), after)) . parse
  where
    go prog book = foldl' (\a _ -> step a book) prog [0..17]


main = interact (show . solve . init)
