from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
from pmaw import PushshiftAPI
from google.cloud import storage
from user_definition import * # date, local directory, list of subreddits

os.environ["no_proxy"]="*" # set this for airflow errors. https://github.com/apache/airflow/discussions/24463

# def create_dir(parent_dir, directory):
#     path = os.path.join(parent_dir, directory)
#     os.makedirs(path, exist_ok=True)

def retrive_7days_reddit_posts(subreddit,end_time,diff=7):
    """
    retrive all posts data from:
    - one subreddit and 
    - one week before the specified date
    arguments: 
    - end_time: in datetime, usually today
    - diff: time interval, by default 7 days
    return
    - df: concated dataframes of reddit posts
    """
    api = PushshiftAPI()
    start_time = end_time - timedelta(days=diff)
    df_lists = []
    for date_counter in range(0,diff): # use for loops for prevent crash
        after = int(start_time.timestamp())
        before = int((start_time + timedelta(days = 1)).timestamp())
        posts = pd.DataFrame(list(api.search_submissions(
                                  subreddit=subreddit,
                                  after=after,
                                  before=before)))
        df_lists.append(posts)
        start_time = start_time + timedelta(days = 1)   
    return pd.concat(df_lists)

# def write_reddit_data_local(df, end_time, subreddit):
#     """write data to local files, for testing only
#     """
#     end_date_str = end_time.strftime("%Y-%m-%d")
#     create_dir(local_data_dir,end_date_str) # create dir if doesn't exist
#     df.to_csv(f"{local_data_dir}/{end_date_str}/{subreddit}.csv",
#               index=False)

def write_reddit_data_gcb(bucket_name, blob_name, service_account_key_file, df):
    """Write and read a blob from GCS using file-like IO"""
    storage_client = storage.Client.from_service_account_json(service_account_key_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("w") as f:
        df.to_csv(f, index=False)