'''
@Author: Rashmi
@Date: 2021-11-11 21:20
@Last Modified by: Rashmi
@Last Modified time: 2021-11-12  21:11
@Title :Write a Python program for Real time stock data ingestion on 
HBase with python's happybase
'''
import happybase as hb
from LogHandler import logger
import requests
import csv
import os

from dotenv import load_dotenv
load_dotenv('.env')
key=os.getenv('API_KEY')

def create_connection():

    """
        Description:
            This function is used for creating connection with hbase.
    """
       
    try:
        conn = hb.Connection()
        conn.open()
        return conn
    except Exception as e:
        logger.error(e)

def create_table():

    """
        Description:
            This function is used for creating hbase table
    """
   
    try:
        connection = create_connection()
        connection.create_table('stockdata_table',{'cf': dict(max_versions=1)})
        logger.info("table created successfully")
       
    except Exception as e: 
        logger.error(e)
        connection.close()

def import_into_hbase():

    """
        Description:
            This function is used for putting csv data into hbase table
    """
     
    try:
        connection = create_connection()
        table = connection.table('stockdata_table')

        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey= key'

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                    table.put(row[0],
                    {'cf:Open': row[1],
                    'cf:High': row[2],
                    'cf:Low': row[3],
                    'cf:Close': row[4],
                    'cf:Volume': row[5]})        
    except Exception as e:
        logger.error(e)
        connection.close()

def display_table():

    """
        Description:
            This function is used for displaying data from hbase table.
    """
      
    try:
        connection = create_connection()
        table = connection.table('stockdata_table')
        for key,data in table.scan():
            id = key.decode('utf-8')
            for value1,value2 in data.items():
                value1 = value2.decode('utf-8')          
                print(id,value1) 

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":

   # create_table()
    #import_into_hbase()
   display_table()
