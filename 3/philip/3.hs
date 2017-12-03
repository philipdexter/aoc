
{-# LANGUAGE TupleSections #-}

import qualified Data.Map.Strict as M
import Data.List (foldl')

data Direction = L | R | U | D

distChange U = 1
distChange D = 1
distChange _ = 0

move L dist (x,y) = (x-dist,y)
move R dist (x,y) = (x+dist,y)
move U dist (x,y) = (x,y+dist)
move D dist (x,y) = (x,y-dist)

opposite L = R
opposite R = L
opposite U = D
opposite D = U

input = 312051 :: Int

find :: Int -> (Int, Int)
find x = go 1 1 (cycle [R,U,L,D]) x (0,0)
  where
    go num dist (cur:directions) target coords | num == target       = coords
                                               | num + dist > target = let cs = go (target) (distChange cur + dist) directions target (move cur dist coords)
                                                                           op = opposite cur
                                                                       in move op (num+dist-target) cs
                                               | otherwise           = go (num+dist) (distChange cur + dist) directions target (move cur dist coords)

between (a,b) (x,y) | x > a = map (,b) [a+1..x]
                    | y > b = map (a,) [b+1..y]
                    | x < a = map (,b) (reverse [x..a-1])
                    | y < b = map (a,) (reverse [y..b-1])

neighbors m (x,y) =
  let cs = [(x-1,y), (x-1,y-1), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y), (x+1,y-1), (x+1,y+1)]
  in map (maybe 0 id . flip M.lookup m) cs

find2 :: Int -> Int
find2 target =
  let init = M.fromList [((0,0),1)]
      dist = 1
      dirs = cycle [R,U,L,D]
      coords = (0,0)
  in go init dist dirs coords
  where
    go map dist (cur:dirs) coords =
      let gountil = move cur dist coords
          tocalc = between coords gountil
          !newmap = foldl' calccoord map tocalc
          calccoord m c = M.insert c (let s = (sum (neighbors m c))
                                       in if s > target then error (show s) else s) m
      in go newmap (distChange cur + dist) dirs gountil

main = print $ find input
