## HHA-data-ingestion
## Import packages
import pandas as pd  # import pandas for general file types
import json  # imoprt json for json files
import bs4  # import bs4 for html files
import requests  # import requests for web requests
import sqlalchemy  # import sqlalchemy for sql queries
from PIL import Image  # import pillow for image files
import pydub  # import pydub for audio files
from pydub.playback import play
import playsound  # import playsound for audio files
import geopandas as gpd  # import geopandas for geospatial files
from google.cloud import bigquery  # import bigquery for bigquery files
import matplotlib
import os
import xlrd  # import xlrd for excel files, tab names
import PyPDF2  # import PyPDF2 for pdf files

# Section 1: 
# Downloaded two datasets from Kaggle called "Best Selling Books" and "Netflix Movies"- combined them into one 
# dataset called "books-movies"
# Saved to data sub-folder in repo
# Bring in the first tab of the dataset and labeling it 'tab1'
tab1 = pd.read_excel('data/books-movies.xls', sheet_name=0)
print(tab1)
## Bringing in tthe second tab of the dataset and labeling it 'tab2'
tab2 = pd.read_excel('data/books-movies.xls', sheet_name=1)
print(tab2)

# Section 2
# Found an open source json API via CMS
# Using request and json packages to import data from the API
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data')
# Next, make sure the variable is assigned to the json file which contains the dataset
apiDataset = apiDataset.json()
print(apiDataset)

# Section 3
# Google Cloud project service account
# Stored authentication key in folder and used .gitignore to hide key 
gcp_project = '507-data-ingestion'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/fizzahzaidi/Downloads/data-ingestion-365018-a78a9c835834.json"
# Use credentials to connect to bigquery client
client = bigquery.Client(project=gcp_project)
# Begin first query using dataset about Birth Data from the CDC (limiting table to 100 rows)
query1 = client.query("SELECT * FROM 'bigquery-public-data.sdoh_cdc_wonder_natality' LIMIT 100")
# Show the results from the first query 
results1 = query1.result()
# Use the results from above to convert to dataframe and assign to variable 'bigquery1'
bigquery1 = results1.to_dataframe()
print(bigquery1)

# Repeat above steps for our second query about Dogecoin (limiting to 100 rows)
query2 = client.query("SELECT * FROM 'bigquery-public-data.crypto_dogecoin' LIMIT 100")
# Show the results from second query with 'results2'
results2 = query2.result()
# Use the results from second query above to convert to dataframe and assign to variable 'bigquery2'
bigquery2 = results2.to_dataframe()
print(bigquery2)