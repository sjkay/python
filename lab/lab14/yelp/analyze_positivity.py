"""Calculate how positive a word is using the Yelp dataset"""

import re
import string
import pyspark

REVIEWS_DATASET = 'reviews.json'
OUTPUT = 'spark-analyze-positivity.out'

REGEX = re.compile('[%s]' % re.escape(string.punctuation))

MIN_OCCURENCES = 500

def avg(iterable):
    total = 0.0
    count = 0
    for val in iterable:
        total += val
        count += 1
    if count > 0:
        return total/count

def mapper(review):
    words = list(set(REGEX.sub(' ', review.text.lower()).split()))
    "*** YOUR CODE HERE ***"
    return [(KEY, VALUE) for word in words]

def filterer(kv_pair):
    key, values = kv_pair
    return len(values) > MIN_OCCURENCES

def reducer(values):
    "*** YOUR CODE HERE ***"
    return 0 # REPLACE THIS LINE

def analyze_positivity(reviews_dataset=REVIEWS_DATASET,
                       output=OUTPUT):
    spark_context = pyspark.SparkContext(appName='AnalyzePositivity')
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(reviews_dataset)

    counts = (reviews.flatMap(mapper)
                     .groupByKey()
                     .filter(filterer)
                     .mapValues(reducer))

    counts.coalesce(1).saveAsTextFile(output)

if __name__ == '__main__':
    analyze_positivity()
