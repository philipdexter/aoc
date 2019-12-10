
import qualified Data.Map.Strict as M

start = 'A'
end = 12994925

data Dir = R | L
dir R = (+1)
dir L = subtract 1

state 'A' 0 = (1, R, 'B')
state 'A' 1 = (0, L, 'F')

state 'B' 0 = (0, R, 'C')
state 'B' 1 = (0, R, 'D')

state 'C' 0 = (1, L, 'D')
state 'C' 1 = (1, R, 'E')

state 'D' 0 = (0, L, 'E')
state 'D' 1 = (0, L, 'D')

state 'E' 0 = (0, R, 'A')
state 'E' 1 = (1, R, 'C')

state 'F' 0 = (1, L, 'A')
state 'F' 1 = (1, R, 'A')

solve = let mem = M.empty
            get = M.findWithDefault 0
            step steps pos mem st | steps < end = let (w,d,s) = state st (get pos mem)
                                                  in step (steps+1) (dir d pos) (M.insert pos w mem) s
                                  | otherwise   = sum (M.elems mem)
        in step 0 0 mem start


main = print solve
