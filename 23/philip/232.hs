

main = let nums = [109900,109917..126900]
       in print . length . filter (\y -> any id [y`mod`x==0 | x <- [2..y-1]]) $ nums
