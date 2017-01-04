--import Text.Regex.Base
--import Text.Regex.TDFA -- cabal update; cabal install regex-tdfa

module Bayes (
) where


-- dummmy = 0
-- 
-- let pattern = "(foo|bar)"
-- let x = "foobarbaz,barbarbar" =~ pattern :: Int
-- 
-- let y = "foobarbaz,barbarbar" =~ pattern :: (MatchOffset, MatchLength)
-- "foobarbaz,barbarbar" =~ pattern :: (MatchOffset, MatchLength)
-- 
-- "this is the pattern the I'm looking for" =~ "the" :: [(MatchOffset,MatchLength)]
-- 
-- "this is the pattern the I'm looking for" =~ "the" :: Int

-- Another Version:

import Text.Regex
-- let x = subRegex (mkRegex "foo[0-9]+") "foo53187barfoofoo329713" "123"


