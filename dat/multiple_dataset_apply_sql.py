import pandas as pd
import os
import glob
import numpy as np
import dat
from datetime import datetime, timedelta, date
import sqlite3
import mysql

def multiple_dataset_apply_mysql(host:str, user:str, password:str, database:str):
    ''' This function reads multiple tables from connected database as parameter 
    then runs all functions on dat package to read table '''

    # db=mysql.connector.connect(host="your host", user="your username", password="your_password",database="database_name")
    db=mysql.connector.connect(host, user, password, database)

    cursor=db.cursor()

    cursor.execute("SHOW TABLES")
    read_table_names = [table_name[0] for table_name in cursor]


    # loop over the list of csv files
    for f in read_table_names:
        # read the csv files
        df = pd.read_csv(f, low_memory=False)
        File_name =  f.split("\\")[-1]
        # Creating dataframes defined on analysis_dict.py file
        for key,value in dat.analysis_dict().items():
            vars()[key] = value(df)
            # Saving dataframes consisting of analysis into a single excel file
            dat.save_dataframe_excel(vars(),f"analysis_{File_name}_{date.today()}")
    return "dataset_analysis_saved"

def multiple_dataset_apply_sqlite(database_name:str):
    ''' This function reads multiple tables from connected database as parameter 
    then runs all functions on dat package to read table '''
    # use glob to get all sql tables
    # in the folder
    con = sqlite3.connect(database_name)
    # con.text_factory = lambda x: str(x, encoding)
    con.text_factory = lambda b: b.decode(errors = 'ignore')
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    # saving all tables of database into a list
    read_table_names = [table_name[0] for table_name in cur]

    # loop over the list of sql tables
    for f in read_table_names:
        print(f)
        # read the sql tables
        df = pd.read_sql(f'SELECT * FROM {f}', con)
        File_name =  f.split("\\")[-1]
        # Creating dataframes defined on analysis_dict.py file
        for key,value in dat.analysis_dict().items():
            vars()[key] = value(df)
            # Saving dataframes consisting of analysis into a single excel file
            dat.save_dataframe_excel(vars(),f"analysis_{File_name}_{date.today()}")
    return "dataset_analysis_saved"

