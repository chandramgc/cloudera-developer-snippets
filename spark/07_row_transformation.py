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
print("First record of orders:\n" + str(orders.first()))
print("First record order status: " + str(orders.map(lambda o: o.split(",")[3]).first()))
orderitems = sc.textFile( myDir + str("/retail_db/order_items"))
print("First record of order item:\n" + str(orderitems.take(1)))
orderItemsMap = orderitems.map(lambda oi: (int(oi.split(",")[1]), float(oi.split(",")[4])))
print("First record of order items map:\n " + str(orderItemsMap.first()))

#sqlContext.clearCache()
print("***********************************************************")
