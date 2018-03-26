from pyspark import SparkConf, SparkContext
conf = ( SparkConf()
	.setMaster("local[*]")
	.setAppName("Girish App")
	.set("spark.executor.memory","1g") )
sc = SparkContext( conf = conf )
myFileDir = "/home/girish/mycode/"
print("***********************************************************")

print("***********************************************************")
