import airflow
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from user_definition import *

from financial_filings_scrape import *
# NOTE : In order to make sure it send configurations requests first, do not import your .py reading from gs.


def _download_financial_filings_data():
    blob_name = f'{folder_name}/{financial_file_name}.csv'
    df = scrape_and_return_financials_df()
    write_csv_to_gcs(bucket_name, blob_name, service_account_key_file, df)
    
#TODO: reddit data pull
# def _download_sf_weather_data():
#     data = filter_history_data(retreive_api_data(noaa_token, noaa_api_url),
#                                three_days_ago)  
#     write_json_to_gcs(bucket_name, f'{three_days_ago}/weather.json', service_account_key_file, data)
    

with DAG(
    dag_id="msds697-task2",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False
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
    download_financial_filing_data = PythonOperator(task_id = "download_financial_filing_data",
                                                  python_callable = _download_financial_filings_data,
                                                  dag=dag)

#TODO
#     download_reddit_data = PythonOperator(task_id = "download_reddit_data",
#                                                     python_callable = _download_reddit_data,
#                                                     dag=dag)
    download_financial_filing_data
    download_reddit_data >> create_insert_aggregate

