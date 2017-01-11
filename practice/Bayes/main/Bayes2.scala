object Parser {

  trait Distributions {
    def rand: String
    def lpdf: String
    def support:String

    def pdf: String = s"exp($lpdf)"
    def typ: String = support match {
      case "unity" => "double"
      case "real" => "double"
      case "real+" => "double"
      case "G0" => "Go"
      case anythingElse => anythingElse 
      //case _ => "IDK!"
    }
  }

  trait StocProc { ??? }

  case class Normal(x: String, m:String, s2:String) extends Distributions {
    val sig = s"sqrt($s2)"
    def lpdf = s"-.5*log(2*pi*$sig) -.5*pow($x-m,2)/(2*$sig)"
    def rand = s"rnorm($m,$sig)"
    def support = "real"
  }

  case class Gamma(x: String, shp:String, rate:String) extends Distributions {
    def lpdf = s"$shp*log($shp) -lgamma($rate) + ($shp-1)*log($x) - $x*$rate"
    def rand = s"rgamma($shp,$rate)"
    def support = "real+"
  }

  ////
  class Bayes (
    val data: Map[String, String],
    val likelihood: Map[String, Distributions],
    val prior: Map[String, Distributions],
    val where: Map[String, String] = Map()
  ) {

    def funSig(fName:String) = {
      val args = data.map(d => d._2 + " " + d._1).mkString(", ")
      s"List $fName($args)"
    }

    // other funs
  }

  val m = Map("y"->Normal("y", "m", "s2"))

  val mod = new Bayes(
    data = Map(
      "y"->"std::vector<double>"
    ),

    likelihood = Map(
      "y"->Normal("y", "mu", "s2")
    ),

    prior = Map(
      "mu"->Normal("mu", "m", "s2"),
      "m"->Normal("m", "0", "s2")
    )
  )

  mod.funSig("fit")
}

// I think this is the best way to go. I can make use of pattern matching
// and OO paradigm. Use this to generate cpp code, then use in Rcpp packages.
// Consider design choices in Stan.

// Eventally:
val mod2 = new Bayes (
  data = Map(
    "M"->"std::vector<double>",
    "N1"->"std::vector<int>",
    "N0"->"std::vector<int>",
    "n1"->"std::vector<int>",
    "x"->"int"
  ),

  likelihood = Map(
    "log(M[s])" -> Normal("log(m[s])","w2"),
    "n1[s]" -> Binom("N1[s]", "p[s]"),
    "log(N1[s]/N0[s])" ->  Normal("z[s]", "sig2")
  ),

  where = Map(
    "p[s]" -> "(mu*v[s]*m[s]) / (2*(1-mu)+mu*m[s])",
    "z[s]" -> "log((2*(1-mu)+mu*m[s])/2)+phi[s]"
  ),

  prior = Map(
    "v[s]"-> "G",
             "G" -> DP("alpha","Beta(aG,bG)"),
    "mu" -> Beta("aMu","bMu"),
    "phi[s]" -> Normal("mPhi", "s2Phi"),
    "sig2" -> InvGamma("aSig", "bSig"),
    "m[s]" -> Gamma("aM", "bM"),
    "w2" -> InvGamma("aW", "bW")
  )
)
