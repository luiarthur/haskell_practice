import Test.HUnit
import Bayes

test0 = TestCase ( assertBool "This should never show" True )
test1 = TestCase ( assertEqual "This should never show test2" 1 (3-2) )

tests = TestList [ TestLabel "test1" test1,
                   TestLabel "test0" test0 ]

main = do
  runTestTT tests

-- to test: 
-- runhaskell -i../main test.hs
