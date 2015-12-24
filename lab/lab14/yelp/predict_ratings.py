import re
import string
import pyspark

REVIEWS_DATASET = 'reviews.json'
ACADEMIC_DATASET = 'yelp_academic_dataset.json'
OUTPUT = 'spark-predict-ratings.out'

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
    words = set(REGEX.sub(' ', review.text.lower()).split())
    "*** YOUR CODE HERE ***"
    return # COPY FROM PREVIOUS QUESTION

def filterer(kv_pair):
    key, values = kv_pair
    return len(values) > MIN_OCCURENCES

def reducer(values):
    "*** YOUR CODE HERE ***"
    return # COPY FROM PREVIOUS QUESTION

def analyze_positivity(spark_context, reviews_dataset=REVIEWS_DATASET):
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(reviews_dataset)

    counts = (reviews.flatMap(mapper)
                     .groupByKey()
                     .filter(filterer)
                     .mapValues(reducer))

    return counts.collect()

def make_predictor(positivities):
    def predictor(review):
        words = set(REGEX.sub(' ', review.text.lower()).split())
        "*** YOUR CODE HERE ***"
        return (KEY, VALUE) # REPLACE THIS LINE
    return predictor

def filter_words(word_positivities):
    avg_pos = avg(word_positivities.values())
    filtered_words = {}
    for word in word_positivities.keys():
        if abs(word_positivities[word] - avg_pos) > 0.15*avg_pos:
            filtered_words[word] = word_positivities[word]
    return filtered_words

def predict_ratings(spark_context, positivities, dataset=ACADEMIC_DATASET):
    sql_context = pyspark.sql.SQLContext(spark_context)

    reviews = sql_context.read.json(dataset).rdd.filter(
        lambda row: row.type == 'review')

    predicted_ratings = reviews.map(make_predictor(positivities)).filter(
            lambda kv_pair: kv_pair[-1] is not None)

    return predicted_ratings

if __name__ == '__main__':
    spark_context = pyspark.SparkContext(appName='PredictRatings')
    word_positivities = dict(analyze_positivity(spark_context))
    filtered_positivities = filter_words(word_positivities)
    ratings = predict_ratings(spark_context, filtered_positivities)
    ratings.coalesce(1).saveAsTextFile(OUTPUT)
