

d "s" = (-1,1,0)
d "sw" = (-1,0,1)
d "nw" = (0,-1,1)
d "n" = (1,-1,0)
d "ne" = (1,0,-1)
d "se" = (0,1,-1)

distance (a,b,c) (x,y,z) = (abs (a-x) + abs (b-y) + abs(c-z)) `div` 2

solve = go (0,0,0) 0 . words
  where go (x,y,z) mdiff (dir:dirs) = let (a,b,c) = d dir
                                          npos = (x+a,y+b,z+c)
                                          mdiff' = max mdiff (distance npos (0,0,0))
                                      in go npos mdiff' dirs
        go pos     mdiff []         = (distance pos (0,0,0), mdiff)


main = interact (show . solve . init)
