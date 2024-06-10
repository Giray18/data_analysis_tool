import pandas as pd
import os
import glob
import numpy as np
import dat
# from save_dataframe_excel import save_dataframe_excel
# from analysis_dict import analysis_dict
# from dat import *
from datetime import datetime, timedelta, date
from sqlalchemy.exc import DatabaseError
import sqlite3
# import mysql
import mysql.connector
import xlsxwriter
import openpyxl
import re


def find_value_sqlite(database_name:str, value:str):
    #Regex pattern for date columns
    pattern_d = re.compile(r"[0-9]{4}.[0-9]{2}.[0-9]{2}.*", re.IGNORECASE)
    pattern_d_alt = re.compile(r"[0-9]{2}.[0-9]{2}.[0-9]{4}.*", re.IGNORECASE)
    # use glob to get all sql tables
    # in the folder
    con = sqlite3.connect(database_name)
    # con.text_factory = lambda x: str(x, encoding)
    con.text_factory = lambda b: b.decode(errors = 'ignore')
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    # saving all tables of database into a list
    read_table_names = [table_name[0] for table_name in cur]
    global frames
    frames = []
    
    for f in read_table_names:
        # read the sql tables by condition of date-time column hold
        df_detect = pd.read_sql(f'SELECT * FROM {f} LIMIT 1', con)
        # Getting list of date-time columns from detection dfs
        col_date = [df_detect[i].name for i in df_detect.columns if pattern_d.match(str(df_detect[i].iloc[0])) or pattern_d_alt.match(str(df_detect[i].iloc[0]))]
        if len(col_date) > 0:
            df = pd.read_sql_query(f"SELECT * FROM {f} WHERE {f}.{col_date[0]} == '{date.today()}'", con)
        else:
            df = pd.read_sql(f'SELECT * FROM {f}', con)
        df_check = pd.DataFrame([value], columns=["value"])
        for k,v in df.items():
            for k1,v1 in df_check.items():
                if v1.isin(v).any():
                    d = {"column" : [k], "table" : [f], "value" : [value]}
                    df_output = pd.DataFrame(data=d)
                    frames.append(df_output)
                    df_ultimate = pd.concat(frames)
    dir = os.path.join("C:\\", "Users\MeliaMuyo\Desktop\ALL\GIRAY\data_analysis_tool", f'{date.today()}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
     # Saving containing cols dataframe 
    writer = pd.ExcelWriter(f"find_value_{value}_{date.today()}.xlsx", engine="xlsxwriter")
    df_ultimate.to_excel(writer,sheet_name="containing_cols")
    writer.close()
    return "value find table saved"




def find_value_mysql(host:str, user:str, password:str, database:str,value:str):
    ''' This function reads multiple tables from connected database 
    then find values searched in database tables '''
    #Regex pattern for date columns
    pattern_d = re.compile(r"[0-9]{4}.[0-9]{2}.[0-9]{2}.*", re.IGNORECASE)
    pattern_d_alt = re.compile(r"[0-9]{2}.[0-9]{2}.[0-9]{4}.*", re.IGNORECASE)
    # use glob to get all sql tables
    # in the folder
    db=mysql.connector.connect(host = str(host), user = str(user), password = str(password), database = str(database))
    cursor=db.cursor()
    cursor.execute("SHOW TABLES")
    myresult = cursor.fetchall()
    # saving all tables of database into a list
    read_table_names = [table_name[0] for table_name in myresult]
    # Creating an empty list to fill pandas dataframe in further steps
    global frames
    frames = []
    # Loop on all tables
    for f in read_table_names:
        # read the sql tables by condition of date-time column hold
        df_detect = pd.read_sql(f'SELECT * FROM {f} LIMIT 1',con=db)
        # Getting list of date-time columns from detection dfs
        col_date = [df_detect[i].name for i in df_detect.columns if pattern_d.match(str(df_detect[i].iloc[0])) or pattern_d_alt.match(str(df_detect[i].iloc[0]))]
        if len(col_date) > 0:
            if (pd.read_sql_query(f"SELECT * FROM {f} WHERE {f}.{col_date[0]} = '{date.today()}'", con=db)).size > 0:
                df = pd.read_sql_query(f"SELECT * FROM {f} WHERE {f}.{col_date[0]} = '{date.today()}'", con=db)
            else:
                df = pd.read_sql(f'SELECT * FROM {f}', con=db) 
        else:
            df = pd.read_sql(f'SELECT * FROM {f}', con=db)
        ####  Old structure can be reshaped later
        # if len(col_date) > 0:
        #     df = pd.read_sql_query(f"SELECT * FROM {f} WHERE {f}.{col_date[0]} == '{date.today()}'", con)
        # else:
        #     df = pd.read_sql(f'SELECT * FROM {f}', con)
        # Creating output dataframe
        df_check = pd.DataFrame([value], columns=["value"])
        # Detect values from read table and save into frames list
        for k,v in df.items():
            for k1,v1 in df_check.items():
                if v1.isin(v).any():
                    d = {"column" : [k], "table" : [f], "value" : [value]}
                    frames.append(d)
    # Changing WD for save output 
    dir = os.path.join("C:\\", "Users\Lenovo\Desktop\exam_eti\containerized_tool\data_analysis_tool", f'{date.today()}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    # Saving containing cols dataframe 
    writer = pd.ExcelWriter(f"find_value_{value}_{date.today()}.xlsx", engine="xlsxwriter")
    df_output = pd.DataFrame(frames)
    df_output.to_excel(writer,sheet_name="found_value")
    writer.close()
    return "value find table saved"