"Counts the number of reviews for each particular restaurant."

import pyspark

REVIEWS_DATASET = 'reviews.json'
OUTPUT = 'spark-count-reviews.out'

def mapper(review):
    return (review.business_id, 1)

def reducer(val1, val2):
    return val1 + val2

def count_reviews(reviews_dataset=REVIEWS_DATASET,
                  output=OUTPUT):
    spark_context = pyspark.SparkContext('local[8]', 'CountReviews')
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(reviews_dataset)

    counts = reviews.map(mapper).reduceByKey(reducer)

    counts.coalesce(1).saveAsTextFile(output)

if __name__ == '__main__':
    count_reviews()
