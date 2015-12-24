"""Counts the number of reviews for each star rating"""

import pyspark

REVIEWS_DATASET = 'reviews.json'
OUTPUT = 'spark-count-by-stars.out'

def mapper(review):
    "*** YOUR CODE HERE ***"
    return None # REPLACE THIS LINE

def reducer(val1, val2):
    "*** YOUR CODE HERE ***"
    return None # REPLACE THIS LINE

def count_by_stars(reviews_dataset=REVIEWS_DATASET,
                   output=OUTPUT):
    spark_context = pyspark.SparkContext(appName='CountStars')
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(reviews_dataset)

    counts = reviews.map(mapper).reduceByKey(reducer)

    counts.coalesce(1).saveAsTextFile(output)

if __name__ == '__main__':
    count_by_stars()
