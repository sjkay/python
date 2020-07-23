import os
import csv
import subprocess
import argparse
import webbrowser
from region import REGION

INSTANCE_TYPE = 't2.micro'
NUM_SLAVES = 1
P_KEY = 'cs61a'
KEY_NAME = 'cs61a'
CREDS = 'credentials.csv'
AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
EMAIL_FILE = 'email.txt'

PY_FILES_DIR = 'yelp'
REVIEWS_DATASET_FILE = 'reviews.json'
ACADEMIC_DATASET_FILE = 'yelp_academic_dataset.json'
REVIEWS_DATASET_URL = 'https://s3-us-west-2.amazonaws.com/yelp-dataset-uc-berkeley/reviews.json'
ACADEMIC_DATASET_URL = 'https://s3-us-west-2.amazonaws.com/yelp-dataset-uc-berkeley/yelp_academic_dataset.json'
DOWNLOAD_DATASET_FILE = 'download_dataset.sh'

COUNT_REVIEWS_FILE = 'count_reviews.py'
COUNT_REVIEWS_OUT = 'spark-count-reviews.out'

COUNT_BY_STARS_FILE = 'count_by_stars.py'
COUNT_BY_STARS_OUT = 'spark-count-by-stars.out'

COUNT_BY_STARS_SQL_FILE = 'count_by_stars_sql.py'
COUNT_BY_STARS_SQL_OUT = 'spark-count-by-stars-sql.out'

ANALYZE_POSITIVITY_FILE = 'analyze_positivity.py'
ANALYZE_POSITIVITY_OUT = 'spark-analyze-positivity.out'

PREDICT_RATINGS_FILE = 'predict_ratings.py'
PREDICT_RATINGS_OUT = 'spark-predict-ratings.out'

BASE = [
    './ec2/spark-ec2',
    '-k', KEY_NAME,
    '-i', P_KEY,
    '--region=' + REGION,
]

def call_launch():
    subprocess.call(BASE + ['--copy-aws-credentials',
                            '--subordinates', str(NUM_SLAVES),
                            '--instance-type=' + INSTANCE_TYPE,
                            'launch', get_email()])

def call_login():
    subprocess.call(BASE + ['login', get_email()])

def call_login2():
    subprocess.call(['ssh', '-i', P_KEY])

def call_get_main():
    subprocess.call(BASE + ['get-main', get_email()])

def call_website():
    url = 'http://{0}:8080'.format(get_main_address())
    print('Opening website for viewing cluster information')
    webbrowser.open(url)
    url = 'http://{0}:4040/jobs/'.format(get_main_address())
    print('Opening website for viewing job progress')
    webbrowser.open(url)

def call_sync():
    subprocess.call("rsync -avz -e 'ssh -i {0}' {1} {2}:".format(
        P_KEY, PY_FILES_DIR, get_main_ip_address()), shell=True)
    subprocess.call("ssh -i {0} {1} './spark-ec2/copy-dir {2}'".format(
        P_KEY, get_main_ip_address(), PY_FILES_DIR), shell=True)

def call_download_dataset():
    cmds = """
        curl -O {0}
        ~/ephemeral-hdfs/bin/hadoop fs -copyFromLocal {1} {1}
        curl -O {2}
        ~/ephemeral-hdfs/bin/hadoop fs -copyFromLocal {3} {3}
    """.format(REVIEWS_DATASET_URL, REVIEWS_DATASET_FILE,
               ACADEMIC_DATASET_URL, ACADEMIC_DATASET_FILE)
    with open(DOWNLOAD_DATASET_FILE, 'w') as cmd_file:
        cmd_file.write(cmds)
    subprocess.call("rsync -avz -e 'ssh -i {0}' {1} {2}:".format(
        P_KEY, DOWNLOAD_DATASET_FILE, get_main_ip_address()), shell=True)
    subprocess.call("ssh -i {0} {1} 'chmod 700 {2}; ./{2}'".format(
        P_KEY, get_main_ip_address(), DOWNLOAD_DATASET_FILE), shell=True)

def run_command(cmd):
    subprocess.call("ssh -i {0} {1} '{2}'".format(
        P_KEY, get_main_ip_address(), cmd), shell=True)

def call_python_script(py_file, out_dir):
    call_sync()
    run_command('MASTER=spark://{0}:7077 ~/spark/bin/spark-submit {1}/{2}'.format(
        get_main_address(), PY_FILES_DIR, py_file))
    run_command('ephemeral-hdfs/bin/hadoop fs -copyToLocal {0} {0}'.format(
        out_dir))
    subprocess.call("rsync -avz -e 'ssh -i {0}' {1}:{2} .".format(
        P_KEY, get_main_ip_address(), out_dir), shell=True)
    run_command('ephemeral-hdfs/bin/hadoop fs -rmr {0}'.format(
        out_dir))

def call_destroy():
    subprocess.call(BASE + ['destroy', get_email()])

def set_aws_credentials():
    with open(CREDS, 'rU') as csvfile:
        for row in csv.reader(csvfile):
            _, key_id, key_secret = row
        os.environ[AWS_ACCESS_KEY_ID] = key_id
        os.environ[AWS_SECRET_ACCESS_KEY] = key_secret

def get_email():
    with open(EMAIL_FILE) as f:
        for line in f:
            email = line.strip().lower()
            if email and email != 'oski@berkeley.edu':
                return email
            else:
                raise ValueError('Must put email in email.txt')

def get_main_address():
    p = subprocess.Popen(BASE + ['get-main', get_email()],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate(
        b"input data that is passed to subprocess' stdin")
    return next(filter(lambda x: x.startswith('ec2'), str(output).split('\\n')))

def get_main_ip_address():
    return 'root@' + get_main_address().split('.')[0][4:].replace('-', '.')

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--launch', action='store_true')
    group.add_argument('--login', action='store_true')
    group.add_argument('--login2', action='store_true')
    group.add_argument('--website', action='store_true')
    group.add_argument('--get_main', action='store_true')
    group.add_argument('--download_dataset', action='store_true')
    group.add_argument('--sync', action='store_true')
    group.add_argument('--count_reviews', action='store_true')
    group.add_argument('--count_by_stars', action='store_true')
    group.add_argument('--count_by_stars_sql', action='store_true')
    group.add_argument('--analyze_positivity', action='store_true')
    group.add_argument('--predict_ratings', action='store_true')
    group.add_argument('--destroy', action='store_true')
    args = parser.parse_args()
    set_aws_credentials()
    if args.launch:
        call_launch()
    elif args.login:
        call_login()
    elif args.login2:
        call_login2()
    elif args.website:
        call_website()
    elif args.get_main:
        call_get_main()
    elif args.download_dataset:
        call_download_dataset()
    elif args.sync:
        call_sync()
    elif args.count_reviews:
        call_python_script(COUNT_REVIEWS_FILE, COUNT_REVIEWS_OUT)
    elif args.count_by_stars:
        call_python_script(COUNT_BY_STARS_FILE, COUNT_BY_STARS_OUT)
    elif args.count_by_stars_sql:
        call_python_script(COUNT_BY_STARS_SQL_FILE, COUNT_BY_STARS_SQL_OUT)
    elif args.analyze_positivity:
        call_python_script(ANALYZE_POSITIVITY_FILE, ANALYZE_POSITIVITY_OUT)
    elif args.predict_ratings:
        call_python_script(PREDICT_RATINGS_FILE, PREDICT_RATINGS_OUT)
    elif args.destroy:
        call_destroy()

if __name__ == '__main__':
    main()
