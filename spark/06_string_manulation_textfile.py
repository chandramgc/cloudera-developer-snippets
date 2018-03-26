from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = ( SparkConf()
	.setMaster("local[*]")
	.setAppName("Girish App")
	.set("spark.executor.memory","6g") )
sc = SparkContext( conf = conf )
sqlContext = SQLContext(sc)

myDir = "/home/girish/mycode/hadoop-developer-snippets/in"

print("***********************************************************")

orders = sc.textFile(myDir + str("/retail_db/orders") )
#orders = sc.textFile("/home/girish/mycode/hadoop-developer-snippets/in/retail_db/orders/part-00000")
print("First record of orders:\n" + str(orders.first()) )

print("***********************************************************")
