import System.IO
import Data.Char -- for toUpper

main = do
  contents <- readFile "testIO.hs"
  putStr contents  
  writeFile "new.txt" (map toUpper contents)
