#!/usr/bin/env python3
from pyspark.sql import Row, SparkSession
from IPython.display import display

spark = SparkSession.builder.master('local[*]').appName('Ex2').getOrCreate()
sc = spark.sparkContext

try :
    lines = sc.textFile('../../data/data_small.csv')
    disasters = lines.map( lambda line : line.split(',') ) \
                   .map( lambda arr : Row( disaster = arr[3], region = arr[6]))
    disasterDF = spark.createDataFrame(disasters)
    disasterDF.createOrReplaceTempView("disasters")
    
    query = ("SELECT disaster, collect_set(region) as regions from disasters "
             "Group by disaster")
    InvIdxDisasterRegionDF = spark.sql(query)
    df = InvIdxDisasterRegionDF.toPandas()
    sc.stop()
except:
    print(err)
    sc.stop()
    
df.head(3)
