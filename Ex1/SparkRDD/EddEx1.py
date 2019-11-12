#!/usr/bin/env python3
import pyspark
from operator import add

sc = pyspark.SparkContext('local[*]')
try :
    lines = sc.textFile('../../data/data_small.csv')
    continent_occurences = lines.map( lambda line : \
                                     (line.split(',')[5],int(line.split(',')[9])))
    invertedIdx = continent_occurences.reduceByKey(add)
    print(invertedIdx.collect())
    sc.stop()
except Exception as e:
    print(e)
    sc.stop()
