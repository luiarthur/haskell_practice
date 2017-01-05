--import Text.Regex.Base
--import Text.Regex.TDFA -- cabal update; cabal install regex-tdfa
-- http://stackoverflow.com/questions/10243290/determining-matching-parenthesis-in-haskell
-- http://www.serpentine.com/blog/2007/02/27/a-haskell-regular-expression-tutorial/
-- https://hackage.haskell.org/package/regex-compat-0.95.1/docs/Text-Regex.html
-- http://stackoverflow.com/questions/21594587/indices-of-all-matches-of-a-regex

module Bayes (
) where

import Text.Regex
import Text.Regex.Base
import Data.Array ((!))

-- finds all pairs of braces
braces :: String -> [(Int,Int)]
braces = go 0 []
  where 
    go _ []      []         = []
    go _ (_:_)   []         = error "unbalanced braces!"
    go j acc     ('{' : cs) =         go (j+1) (j:acc) cs
    go j []      ('}' : cs) = error "unbalanced braces!"
    go j (i:is)  ('}' : cs) = (i,j) : go (j+1) is      cs
    go j acc     (c   : cs) =         go (j+1) acc     cs


-- replaces all "\n" with ";"
strip :: String -> String
strip s = do
  let rgx = makeRegex "\n" :: Regex
  subRegex rgx s ";"

-- gets specified fields enclosed in braces from string
getField :: String -> String -> String
getField s field = do
  let rgx = makeRegex (field ++ "\\s*\\{[^\\{]+}") :: Regex
  let Just(_,dat,_,_) = matchRegexAll rgx (strip s)
  dat

-- quick tests:
-- import System.IO
-- s <- readFile "../resource/test.model"
