#!/usr/bin/env python3
from pyspark.sql import Row, SparkSession
from IPython.display import display

spark = SparkSession.builder.master('local[*]').appName('Ex1').getOrCreate()
sc = spark.sparkContext

try :
    lines = sc.textFile('../../data/data_small.csv')
    continent_occurences = lines.map( lambda line : line.split(',') ) \
                   .map( lambda arr : Row( continent = arr[5], occurences = int(arr[9])))
    continent_occurences_df = spark.createDataFrame( continent_occurences )
    continent_occurences_df.createOrReplaceTempView("continents")
    
    query = ("SELECT continent,SUM(occurences) as n_occurences from continents "
             "Group by continent")
    InvIdxContinentOccurencesDF = spark.sql(query)
    display(InvIdxContinentOccurencesDF.toPandas())
    sc.stop()
except:
    print(err)
    sc.stop()

