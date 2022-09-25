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
import xlrd  # import xlrd for excel files, tab names
import PyPDF2  # import PyPDF2 for pdf files

## Section 1: 
## Downloaded dataset from Kaggle, "Netflix Disney+ Prime Video Hulu Shows Collection"
## Saved to data sub-folder in repo
## Define xls spreadsheet file with 'xls'
xls = 
