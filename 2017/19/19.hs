
import Data.Array.ST
import Data.Array.MArray
import GHC.Arr

solve :: String -> String
solve i = (runSTArray (go (parse (lines i))) :: GHC.Arr.Array (Int,Int) Char) `seq` "a"
  where
    parse :: [String] -> STArray _ (Int,Int) Char
    parse = newListArray ((0,10)::(Int,Int))
    go arr = do
      writeArray arr (0,0) 'c'
      return arr



main = interact ( show . solve . init )
