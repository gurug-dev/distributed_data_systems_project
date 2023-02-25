import airflow
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from user_definition import *

from financial_fillings_scrape import *
from reddit_calls import *
import os
import shutil


# NOTE : In order to make sure it send configurations requests first, do not import your .py reading from gs.

def rm_r(path):
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)
        
def _clear_temp_folders():
    for path in paths_to_clear:
        rm_r(path)
        
def _download_financial_filings_data():
    blob_name = f'{folder_name}/{financial_file_name}.csv'
    df = scrape_and_return_financials_df()
    write_csv_to_gcs(bucket_name, blob_name, service_account_key_file, df)

# reddit data pull by Youshi
def _download_reddit_data():
    """wrapper function for all the steps
    for testing only
    """
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    for subreddit in list_of_reddits:
        blob_name = f'{yesterday_str}/{subreddit}.csv'
        df = retrive_7days_reddit_posts(subreddit, yesterday)
        write_reddit_data_gcb(bucket_name, blob_name, service_account_key_file, df)
    

with DAG(
    dag_id="msds697-task2",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    schedule_interval='@daily' # reddit data is planned to be called weekly, change function schedule?
) as dag:

    create_insert_aggregate = SparkSubmitOperator(
        task_id="aggregate_creation",
        packages="com.google.cloud.bigdataoss:gcs-connector:hadoop2-1.9.17,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1",
        exclude_packages="javax.jms:jms,com.sun.jdmk:jmxtools,com.sun.jmx:jmxri",
        conf={"spark.driver.userClassPathFirst":True,
             "spark.executor.userClassPathFirst":True,
            #  "spark.hadoop.fs.gs.impl":"com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem",
            #  "spark.hadoop.fs.AbstractFileSystem.gs.impl":"com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS",
            #  "spark.hadoop.fs.gs.auth.service.account.enable":True,
            #  "google.cloud.auth.service.account.json.keyfile":service_account_key_file,
             },
        verbose=True,
        application='aggregates_to_mongo.py'
    )
    clear_tmp_folders = PythonOperator(task_id = "clear_tmp_folders",
                                                  python_callable = _clear_temp_folders,
                                                  dag=dag)
    
    download_financial_filing_data = PythonOperator(task_id = "download_financial_filing_data",
                                                  python_callable = _download_financial_filings_data,
                                                  dag=dag)

    download_reddit_data = PythonOperator(task_id = "download_reddit_data",
                                                    python_callable = _download_reddit_data,
                                                    dag=dag)
    clear_tmp_folders>> [download_financial_filing_data, download_reddit_data] >> create_insert_aggregate
