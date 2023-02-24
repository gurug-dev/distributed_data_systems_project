from datetime import date, datetime, timedelta
import os



#TODO:
financial_folder = 'SEC_FILINGS'
email="mkarri@usfca.edu"
website="https://www.usfca.edu/"
headers = { "User-Agent": f"{website} {email}"}
financial_file_name = "Russell_3000_Companies_Filings"
bucket_name = os.environ.get("GS_BUCKET_NAME")
# service_account_key_file = os.environ.get("GS_SERVICE_ACCOUNT_KEY_FILE")
service_account_key_file = '/Users/gurug/USF/airflow_test/dds-msds-project-1040f42d6684.json'

mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password =  os.environ.get("MONGO_PASSWORD")
mongo_ip_address = os.environ.get("MONGO_IP")
database_name = os.environ.get("MONGO_DB_NAME")
collection_name = os.environ.get("MONGO_COLLECTION_NAME")

folder_name = date.today()

# variables associated with reddit call
yesterday = datetime.today() - timedelta(days=1)
client_secret = 'klhppqo7oLptclnKbyYxcf5ZaSWnYQ'
client_id = 'NshKC-eP4HnQuF_wNzQNGA'
user_agent='Stocks'
list_of_reddits = ['wallstreetbets','stocks','pennystocks','DueDiligence','smallstreetbets','shroomstocks','traders',\
                   'SPACs','ValueInvesting','UndervaluedStonks','investing','SecurityAnalysis',\
                   'Wallstreetbetsnew','UnderValuedStocks','EducatedInvesting','RichTogether',\
                   'greeninvestor','stonks','investing_discussion','options','StockMarket','InvestmentClub',\
                   'RobinHood']

# # two_days_ago = date.today() - timedelta(days=4)
# # three_days_ago = date.today() - timedelta(days=5) 
# two_days_ago = '2023-01-26'
# three_days_ago = '2023-01-25'

# sf_data_url = "data.sfgov.org"
# data_limit = 200000
# sf_data_sub_uri = "gnap-fj3t"
# sf_data_app_token = os.environ.get("SF_DATA_TOKEN")

# noaa_token = os.environ.get("NOAA_TOKEN")
# # station_id = "GHCND:USW00023272"
# # dataset_id = "GHCND"
# # location_id = "CITY:US060031"
# noaa_endpoint = f"data?datasetid={dataset_id}&datatypeid=PRCP&station_id={station_id}&startdate={three_days_ago}&enddate={two_days_ago}"
# noaa_api_url = f"https://www.ncei.noaa.gov/cdo-web/api/v2/{noaa_endpoint}"

# bucket_name = os.environ.get("GS_BUCKET_NAME")
# service_account_key_file = os.environ.get("GS_SERVICE_ACCOUNT_KEY_FILE")

