--import Text.Regex.Base
--import Text.Regex.TDFA -- cabal update; cabal install regex-tdfa
-- http://stackoverflow.com/questions/10243290/determining-matching-parenthesis-in-haskell
-- http://www.serpentine.com/blog/2007/02/27/a-haskell-regular-expression-tutorial/
-- https://hackage.haskell.org/package/regex-compat-0.95.1/docs/Text-Regex.html
-- http://stackoverflow.com/questions/21594587/indices-of-all-matches-of-a-regex

module Bayes (
) where

braces :: String -> [(Int,Int)]
braces = go 0 [] -- fn named go, which takes the starting idx and accumulator of paren idx []
  where 
    go _ []      []         = []
    go _ (_:_)   []         = error "unbalanced braces!"
    go j acc     ('{' : cs) =         go (j+1) (j:acc) cs
    go j []      ('}' : cs) = error "unbalanced braces!"
    go j (i:is)  ('}' : cs) = (i,j) : go (j+1) is      cs
    go j acc     (c   : cs) =         go (j+1) acc     cs

-- braces "abd{adsad}{def}"

-- import Text.Regex
-- import Text.Regex.Base
-- import Data.Array ((!))
-- let pat = mkRegex "[()]"
-- splitRegex pat "abc(bla(beef))def" 

-- let pat = makeRegex "[()]" :: Regex
-- let m = matchAll pat "abc(bla(beef))def"
-- let x = map (\(a,b) -> a :: Int) $ map(!0) m


