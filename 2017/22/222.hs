

import qualified Data.Map.Strict as M
import Data.List
import Data.Ord (comparing)


data Dir = Up | Left | Down | Right deriving (Show,Enum)
turnLeft d = toEnum ((fromEnum d + 1) `mod` 4) :: Dir
turnRight d = toEnum ((fromEnum d - 1) `mod` 4) :: Dir
turnAround d = toEnum ((fromEnum d + 2) `mod` 4) :: Dir

infected '#' = True
infected _   = False

newDir '#' = turnRight
newDir '.' = turnLeft
newDir 'W' = id
newDir 'f' = turnAround

swap '.' = 'W'
swap 'W' = '#'
swap '#' = 'f'
swap 'f' = '.'

update (x,y) Up = (x,y-1)
update (x,y) Down = (x,y+1)
update (x,y) Main.Left = (x-1,y)
update (x,y) Main.Right = (x+1,y)

solve = go (12,12) Up 10000000 . parse
  where
    parse i = foldl' (\m (k,v) -> M.insert k v m) M.empty [ ((y,x),c) | (x,l) <- zip [0..] (lines i), (y,c) <- zip [0..] l ]
    go _ _ 0 _ = 0
    go pos dir n m = let c = M.findWithDefault '.' pos m
                         newdir = newDir c dir
                         m' = M.fromList [(pos,swap c)] `M.union` m
                     in (if infected (swap c) then 1 else 0) + go (update pos newdir) newdir (n-1) m'

main = interact ( show . solve . init )
