from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = ( SparkConf()
	.setMaster("local[*]")
	.setAppName("Girish App")
	.set("spark.executor.memory","1g") )
sc = SparkContext( conf = conf )
sqlContext = SQLContext(sc)

myDir = "/home/girish/mycode/hadoop-developer-snippets/in"

print("***********************************************************")

linesList = ["How are number 1", "How are number 2", "How are number 3","How are number 4"]
lines = sc.parallelize(linesList)
print("Print all data in LinesList:")
for i in lines.collect(): print(i)
words = lines.flatMap(lambda l: l.split(" "))
print("Print all data in words:")
for i in words.collect(): print(i)
print("***********************************************************")
