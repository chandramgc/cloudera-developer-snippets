from pyspark import SparkConf, SparkContext
conf = ( SparkConf()
	.setMaster("local[*]")
	.setAppName("Girish App")
	.set("spark.executor.memory","1g") )
sc = SparkContext( conf = conf )
print("---------------------------------------------------")
productsRaw = open("/home/girish/mycode/retail_db/products/part-00000").read().splitlines()
print("Type of productsRaw: " + str(type(productsRaw)) )
productsRDD = sc.parallelize(productsRaw)
print("Type of productsRDD: " + str(type(productsRDD)) )
print("Get first record of productsRDD:\n" + str(productsRDD.first()) )
print("Get top 10 record of productsRDD:\n" + str(productsRDD.take(10)) )
print("Get count of records in productsRDD\n" + str(productsRDD.count()) )
print("---------------------------------------------------")