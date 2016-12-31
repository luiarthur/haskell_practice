module Human (
  Person(..)
) where

data Person = Person { 
                firstName :: String,
                lastName :: String,
                age :: Int 
              } deriving (Show)
