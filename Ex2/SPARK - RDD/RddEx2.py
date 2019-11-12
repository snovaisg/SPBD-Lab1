import pyspark
from operator import add

sc = pyspark.SparkContext('local[*]')
try :
    lines = sc.textFile('../../data/data_small.csv')
    disasters_regions = lines.map( lambda line : ( line.split(',')[3], line.split(',')[6] ) )
    invIndexDisastersRegions = disasters_regions.groupByKey().mapValues(set)
    for disaster,region in invIndexDisastersRegions.take(5):
        print(f"{disaster} : {region}\n")
    sc.stop()
except Exception as e:
    print(e)
    sc.stop()
