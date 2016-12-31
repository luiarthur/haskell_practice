import Test.HUnit
import Human

test1 = TestCase ( assertEqual "for test1" 1 (3-2) )
test2 = TestCase ( assertBool "for test2" False )
test3 = TestCase ( assertBool "for test3" True )

tests = TestList [ TestLabel "test1" test1,
                   TestLabel "test2" test2,
                   TestLabel "test2" test3 ]

main = do
  runTestTT tests


-- to test: 
-- runhaskell -i../main test.hs
