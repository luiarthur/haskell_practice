import re

def parseFile(path):
    f = open(path)
    fileContents = f.read()
    f.close()
    return fileContents


s = parseFile("../resource/test2.model")

r = re.compile(r'ha{2}')
h = r.search('I am haha')

print h
