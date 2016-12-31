import System.Random

let initSeed = mkStdGen 1
let (x,newSeed) = randomR (1,6) initSeed
randomR (1,6) newSeed


