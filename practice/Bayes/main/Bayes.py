import re


def parseFile(path):
    f = open(path)
    fileContents = f.read()
    f.close()
    #
    noReturn = re.sub('\n', ';', fileContents)
    noSpace = re.sub('\s+', '', noReturn)
    cleanFileContents = re.sub(';+', ';', noSpace)
    #
    return cleanFileContents


def getField(s, field):
    return re.search(field + "\{[^{]+\}", s).group()


## Tests:

s = parseFile("../resource/test2.model")


#def getParam(s):
data = getField(s, "Data")
datum = re.match(";(^;)+;", data) # FIXME
