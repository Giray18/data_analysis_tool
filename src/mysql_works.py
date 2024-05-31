import mysql.connector
import dat
import os
from datetime import datetime, timedelta, date
import openpyxl
import xlsxwriter
import pandas as pd
import numpy as np
import re
import json

# mydb = mysql.connector.connect(user = os.environ['MYSQLSERVER_USER'], password = os.environ['MYSQLSERVER_PASS'],
#                               host ='localhost',
#                               database ='sakila')
print("davar")

df = dat.df_read_aws('merkle-de-interview-case-study/de','item.csv')

functions_df_names = dat.analysis_dict()

for key,value in functions_df_names.items():
    # Creating dataframes defined on analysis_dict.py file
    vars()[key] = value(df)

dat.save_dataframe_excel(globals(),f"analysis_dataset_{date.today()}")
# mycursor = mydb.cursor()

# user = os.environ['MYSQLSERVER_USER']
# password = os.environ['MYSQLSERVER_PASS']

# dat.multiple_dataset_apply_sql.multiple_dataset_apply_containing_cols_mysql('localhost','root','Dingilaz55!','sakila')