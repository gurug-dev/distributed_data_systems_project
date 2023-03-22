from datetime import date, datetime, timedelta
import os



#TODO:
financial_folder = 'SEC_FILINGS'
email="mkarri@usfca.edu"
website="https://www.usfca.edu/"
headers = { "User-Agent": f"{website} {email}"}
financial_file_name = "Russell_3000_Companies_Filings"
bucket_name = os.environ.get("GS_BUCKET_NAME")
service_account_key_file = os.environ.get("GS_SERVICE_ACCOUNT_KEY_FILE")

paths_to_clear = ["./datasets/INDICES","./datasets/RAW_FILINGS","./datasets/FILINGS_METADATA"]

mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password =  os.environ.get("MONGO_PASSWORD")
mongo_ip_address = os.environ.get("MONGO_IP")
# mongo_ip_address = 'localhost'

database_name = os.environ.get("MONGO_DB_NAME")
collection_name_finance = "financial"
collection_name_reddit = "reddit"

REF_STRING = "mongodb+srv://admin:<password>@msds697-cluster.qzgwq.mongodb.net/"
MONGO_DB_NAME = "msds697_project"
        
# variables associated with reddit call
yesterday = datetime.today() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
client_secret = 'klhppqo7oLptclnKbyYxcf5ZaSWnYQ'
client_id = 'NshKC-eP4HnQuF_wNzQNGA'
user_agent='Stocks'
# list_of_reddits = ['wallstreetbets','stocks','pennystocks','DueDiligence','smallstreetbets','shroomstocks','traders',\
#                    'SPACs','ValueInvesting','UndervaluedStonks','investing','SecurityAnalysis',\
#                    'Wallstreetbetsnew','UnderValuedStocks','EducatedInvesting','RichTogether',\
#                    'greeninvestor','stonks','investing_discussion','options','StockMarket','InvestmentClub',\
#                    'RobinHood']

list_of_reddits = ['wallstreetbets'] #TEST

