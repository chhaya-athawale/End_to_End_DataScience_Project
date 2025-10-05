import os
import sys
from src.DATA_SCIENCE_PROJECT.pipelines.exception import CustomException
from src.DATA_SCIENCE_PROJECT.pipelines.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')



def read_sql_data():
    logging.info("Reading SQL database started")

    # Debugging: check env variables
    print("Host:", host)
    print("User:", user)
    print("DB:", db)
    
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established: {mydb}")

        df=pd.read_sql_query('Select * from fraud_detection',mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)