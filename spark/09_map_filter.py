
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

orders = sc.textFile( myDir + str("/retail_db/orders"))
ordersComplete = orders.filter(lambda o: o.split(",")[3] == "COMPLETE")
print("Get first 10 complete status:")
for i in ordersComplete.take(10): print(i)
ordersCompleteClosed = orders.filter(lambda o: o.split(",")[3] == "COMPLETE" or o.split(",")[3] == "CLOSED")
for i in ordersCompleteClosed.take(10): print(i)
ordersCompleteClosedDate = orders. \
	filter(lambda o: \
		(o.split(",")[3] == "COMPLETE" or o.split(",")[3] == "CLOSED") and \
		(o.split(",")[1][:7] == "2014-01") \
	)
for i in ordersCompleteClosedDate.take(10): print(i)
ordersCompleteClosedIn = orders.filter(lambda o: o.split(",")[3] in ["COMPLETE" , "CLOSED"])
for i in ordersCompleteClosedIn.take(10): print(i)

print("***********************************************************")
