import System.IO
s <- readFile "../resource/test2.model"

let dat = getField s "Data"
let like = getField s "Likelihood"
let prior = getField s "Prior"



