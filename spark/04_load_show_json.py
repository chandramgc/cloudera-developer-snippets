from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = ( SparkConf()
	.setMaster("local[*]")
	.setAppName("Girish App")
	.set("spark.executor.memory","1g") )
sc = SparkContext( conf = conf )
sqlContext = SQLContext(sc)

myDir = "/home/girish/mycode"

print("***********************************************************")

dataLoad = sqlContext.load("/home/girish/mycode/hadoop-developer-snippets/in/retail_db_json/order_items", "json")
print("Data of Json file:\n")
dataLoad.show()

print("***********************************************************")
