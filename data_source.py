import pandas as pd
import numpy as np
import requests
import loguru


#import the logger
logger = loguru.logger()

# this is the file that extracts data from the internet 
def extract(url:str,body:dict):
  """
  extract financial data using the API
  """
  logger.info("starting the extraction for the Api ")

def transformations(df:pd.DataFrame):
  """
  Contains the logic that transform data from the raw phase to the final 
  
  """


def load_or_wwrite_data()