import re

rvSupport = {'Beta': 'unity', 
             'Normal': 'real', 
             'Gamma': 'positiveReal',
             'InvGamma': 'positiveReal',
             'DP': 'G0'}

rvType = {'unity': 'double', 
          'real': 'double',
          'positiveReal': 'double',
          'G0': 'G0'}


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


# match between ";"
reElem = re.compile("(?<=;)[^;]+(?=;)")


def getRcppFunArg(s):
    data = getField(s, "Data")
    data_elem = reElem.findall(data)
    sep = map(lambda x: str.split(x,":"), data_elem)
    param = [ e[0] for e in sep ]
    paramType = [re.sub("vector","std::vector",e[1]) for e in sep]
    args = map(lambda z: z[0] + " " + z[1], zip(param,paramType))
    return str.join(", ", args)


# match the distribution
reDistr = re.compile("\w+(?=\()")

# get G0 for DP
reDPType = re.compile("(?<=G0=)\w+(?=\()")

def getRcppReturnType(s):
    prior = getField(s, "Prior")
    prior_elem = reElem.findall(prior)
    sep = map(lambda x: str.split(x,"~"), prior_elem)
    distr = map(lambda x: reDistr.search(x[-1]).group() , sep)
    # if any of them are DP, then redo those and get reDPType
    indDP = [ i for i in xrange(len(distr)) if distr[i]=='DP']
    for i in indDP:
        distr[i] = reDPType.search(sep[i][-1]).group()
    retType = map(lambda d: rvType[rvSupport[d]] , distr)
    retContainer = [None] * len(distr)
    # FIXME: STOPPED HERE
    for r in retType:
        retContainer = "NumericVector"
    return retContainer

## Tests:

s = parseFile("../resource/test2.model")
getRcppFunArg(s)
getRcppReturnType(s)


