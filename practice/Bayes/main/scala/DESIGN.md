```scala
trait Distributions {
  // define for each type
  def rand: String // defines the random number generator
  def lpdf: String // defines the logpdf
  def support:String // defines the support

  // to be define in the trait
  def pdf: String = s"exp($lpdf)"
  def typ: String // the computational type of the RV which is 
                  // inferred using a pattern match of the support
}

// defines the model
class Bayes (
  val data: Map[String, String],
  val likelihood: Map[String, Distributions],
  val prior: Map[String, Distributions],
  val where: Map[String, String] = Map()
) {

  // returns the entire Rcpp function
  def generateRcppFunc(funName:String): String

  // returns the Rcpp function sig 
  private def funSig(funName:String): String

  // returns the core of the function
  private def funImpl: String

  // returns the fun args and types (data, prior param, mcmc its, etc, tuning params)
  private def funArgs: String

  // returns a list of the parameters and their types in MCMC
  private def funParams: String

  // returns a list of the tuning parameters and their types in MCMC
  private def funTunes: String

  // returns a list of the update functions
  private def funUpdates: String

  // predefined template codes
  val gibbs: String
  val metropolis: String
  val metLogit: String
  val neal8: String
  val rig: String
  val wsampleIdx: String
  val header: String
  val exporter: String
  val state: String = "struct State{}"
}
```
