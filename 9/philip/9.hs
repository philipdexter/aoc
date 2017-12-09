


solve = go 0 False
  where go curGroupScore False (x:xs) =
          case x of
            '{' -> go (curGroupScore+1) False xs
            '<' -> go curGroupScore True xs
            '}' -> curGroupScore + go (curGroupScore-1) False xs
            ',' -> go curGroupScore False xs
        go curGroupScore True (x:xs) =
          case x of
            '>' -> go curGroupScore False xs
            '!' -> go curGroupScore True (drop 1 xs)
            _   -> go curGroupScore True xs
        go _ _ [] = 0

solve2 = go False
  where go False (x:xs) =
          case x of
            '{' -> go False xs
            '<' -> go True xs
            '}' -> go False xs
            ',' -> go False xs
        go True (x:xs) =
          case x of
            '>' -> go False xs
            '!' -> go True (drop 1 xs)
            _   -> 1 + go True xs
        go _ [] = 0


main = interact (show . solve2 . init)
