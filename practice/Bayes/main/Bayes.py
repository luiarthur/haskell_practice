import re

rvSupport = {
    'Beta': 'unity', 
    'Normal': 'real', 
    'Gamma': 'positiveReal',
    'InvGamma': 'positiveReal',
    'DP': 'G0'
}

rvType = {
    'unity': 'double', 
    'real': 'double',
    'positiveReal': 'double',
    'G0': 'G0'
}


logpdf = {
    'Normal(x,m,s2)': '-.5*(2*pi*s2) -.5*(x-m)^2/s2',
}

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
    args = map(lambda z: z[1] + " " + z[0], zip(param,paramType))
    return str.join(", ", args)


# match the distribution
reDistr = re.compile("\w+(?=\()")

# get G0 for DP
reDPType = re.compile("(?<=G0=)\w+(?=\()")

def getRcppFunSig(s, fName):
    return "List " + fName + "(" + getRcppFunArg(s) + ")"


# get param
reParam = re.compile("\w+(?=(\[|~)?)") # check

def getRcppParamType(s):
    prior = getField(s, "Prior")
    prior_elem = reElem.findall(prior)
    sep = map(lambda x: str.split(x,"~"), prior_elem)
    pType = [ "NumericMatrix" if ("[" in p[0]) else "NumericVector" for p in sep ]
    zs = zip(pType, map(lambda p: reParam.search(p[0]).group(), sep))
    return map(lambda z: z[0] + " " + z[1] , zs)


# STOPPED HERE FIXME

def getSamplingDen(s):
    like = getField(s, "Likelihood")
    like_elem = reElem.findall(like)
    arg = map(lambda x: str.split(x,"|")[0], like_elem)
    den = map(lambda x: str.split(x,"~")[-1], like_elem)
    pass


def getFullCond(s):
    pass


## Tests:

s = parseFile("../resource/test2.model")
getRcppFunArg(s)
getRcppParamType(s)
getRcppFunSig(s, "myFunc")

