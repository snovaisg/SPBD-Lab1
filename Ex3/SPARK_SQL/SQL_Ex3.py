from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import udf
from utils import *
import pandas as pd


spark = SparkSession.builder.master('local[*]').appName('words').getOrCreate()
sc = spark.sparkContext
spark.udf.register("fillaffected",fillaffected)
spark.udf.register("fillnan",fillnan)
try :
    lines = sc.textFile('../../data/data_small.csv')
    
    data = lines.filter( lambda line : len(line) > 0 )   \
                        .map( lambda line : line.split(',') ) \
                        .map( lambda arr : Row( dec = arr[0][:-1], DT = arr[3], continent = arr[5], \
                                               inj = arr[11], deaths = arr[10], affected = arr[14]))
    DF = spark.createDataFrame( data )
    
    DF.createOrReplaceTempView("ini")
    
    DF=spark.sql("select DT,continent,fillnan(dec) as dec,fillnan(inj) as inj,fillnan(deaths) as deaths,fillnan(affected) as affected from ini")
    DF.createOrReplaceTempView("dis")
    
    sumaff=spark.sql("select DT,continent,dec,inj,deaths,fillaffected(inj,deaths,affected) as affected from dis")
    sumaff.createOrReplaceTempView("dis")
    sumall=spark.sql("select continent,DT,dec,sum(inj)/(sum(affected)+0.001) as inj_prob,sum(deaths)/(sum(affected)+0.001) as death_prob from dis group by DT,continent,dec")

    df=sumall.toPandas()
    
    sc.stop()
except Exception as e:
    print(e)
    sc.stop()