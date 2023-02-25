import re
import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

from google.cloud import storage

from user_definition import *

os.environ["no_proxy"]="*"


def create_config_json():
    rusell_3000 = pd.read_csv("Russell 3000 - Google Spreadsheet - Sheet 1.csv")
    list_of_stocks = list(rusell_3000.Ticker.unique())
    
    with open("financialcik.json", encoding='utf-8', errors='ignore') as json_data:
         data = json.load(json_data, strict=False)

    cik_data = [(data[x]['ticker'],data[x]['cik_str']) for x in data.keys()]
    cik_data_dict = {}

    for cik in cik_data:
        cik_data_dict[cik[0]] = cik[1]
    rusell_ciks = []
    rusell_ciks_stock = []

    for stock in list_of_stocks:
        try:
            rusell_ciks.append(cik_data_dict[stock])
            rusell_ciks_stock.append(stock)
        except:
            pass

    # with open('edgar-crawler/config.json','r') as f:
    with open('config.json','r') as f:

        dict1 = json.loads(f.read())
    dict1['edgar_crawler']['cik_tickers'] = list(rusell_ciks)
    # with open('edgar-crawler/config.json','w') as outfile:
    with open('config.json','w') as outfile:
        json.dump(dict1, outfile)
    

def financialinfo_scraping(filings):
    filename = list(filings.filename.unique())
    seven = []
    #seven_a = []
    for file in filename:
        with open('datasets/RAW_FILINGS/{}'.format(file),'r') as f:
            
            #print(file)
            raw_file = f.read()
            raw_file_parsed = BeautifulSoup(raw_file, 'html.parser')
            seven.append(raw_file_parsed.get_text())

    filings['text'] = seven
    return filings

def return_financial_df(filings):
    new_file = financialinfo_scraping(filings)
    return new_file

def write_csv_to_gcs(bucket_name, blob_name, service_account_key_file, df):
    """Write and read a blob from GCS using file-like IO"""
    storage_client = storage.Client.from_service_account_json(service_account_key_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("w") as f:
        df.to_csv(f, index=False)
        
def scrape_and_return_financials_df():
    create_config_json()
    os.system('python edgar_crawler.py')
    filings = pd.read_csv('datasets/FILINGS_METADATA.csv')
    financial_df = return_financial_df(filings)
    return financial_df
    