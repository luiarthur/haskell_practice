def parseFile(path: String) =
  io.Source.fromFile(path).getLines.mkString(";").filter(_!=' ')


def getField(s:String, field:String) = {
  val re= ( field + """\s*\{[^\{]+\}""" ).r
  re.findAllIn(s).mkString
}

def genRcppFunArgs(model: String) = {
  val data = getField(model,"Data")
  val reDatum = """Data\{;(.*);\}""".r
  val datum = data match { case reDatum(x) => x; case _ => "bla" }

  val datls = datum.split(';').toList
  val fm = datls map { _.split(":").toList }
  val reVector = """vector<(.*)>""".r
  val paramTypes = fm map { x => x.last match {
    case reVector(y) => "std::vector<" + y + ">"
    case z => z
  }}
  val params = fm map { _.head }
  (params zip paramTypes) map {z => z._1 + " " + z._2} mkString(", ")
}

// stopped here: requires parsing the prior to see what the types are
def genRcppReturnType(model: String) = {
  val prior = getField(model,"Prior")
  val params = prior.split(";").toList
}

def genRcppFunSig(model: String, fName: String) {
  lazy val funArgs = genRcppFunArgs(model)
  lazy val fReturnType = genRcppReturnType(model)

  fReturnType + fName + "(" + funArgs + ")"
}

val s = parseFile("../resource/test2.model")
