"""Count the number of reviews for each star rating using SQL"""

import pyspark

REVIEWS_DATASET = 'reviews.json'
OUTPUT = 'spark-count-by-stars-sql.out'

def sql_query():
    "*** YOUR CODE HERE ***"
    return 'YOUR SQL QUERY HERE'

def count_by_stars_sql(reviews_dataset=REVIEWS_DATASET,
                       output=OUTPUT):
    spark_context = pyspark.SparkContext(appName='CountStarsSQL')
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(reviews_dataset)
    reviews.registerTempTable('reviews')

    counts = sql_context.sql(sql_query())

    counts.coalesce(1).rdd.saveAsTextFile(output)

if __name__ == '__main__':
    count_by_stars_sql()
