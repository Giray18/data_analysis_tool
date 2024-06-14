import numpy as np
import sys
# sys.path.insert(0, 'C:/Users/Lenovo/Desktop/exam_eti/containerized_tool/data_analysis_tool')
sys.path.insert(0, '/src/src')
import pandas as pd
import dat
from collections import defaultdict
import json
import re
import os
import mysql.connector
from datetime import datetime, timedelta, date


class mysql_profiler:
    '''Class to create quick profiling of tables located on mysql server'''

    def __init__(self,host,user,password,database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def multiple_dataset_apply_mysql(self):
        ''' This function reads multiple tables from connected database as parameter 
        then runs all functions on dat package to read table '''

        #Regex pattern for date columns
        pattern_d = re.compile(r"[0-9]{4}.[0-9]{2}.[0-9]{2}.*", re.IGNORECASE)
        pattern_d_alt = re.compile(r"[0-9]{2}.[0-9]{2}.[0-9]{4}.*", re.IGNORECASE)

        # Creating connection string
        db=mysql.connector.connect(host = str(self.host), user = str(self.user), password = str(self.password), database = str(self.database))
        cursor=db.cursor()
        cursor.execute("SHOW TABLES")
        myresult = cursor.fetchall()

        # saving all tables of database into a list
        read_table_names = [table_name[0] for table_name in myresult]

        # Dict for dataframes that has read from database
        dataframes_dict = {}

        # Creating working directory for daily partitioning
        dir = os.path.join("C:\\", "Users\Lenovo\Desktop\exam_eti\containerized_tool\data_analysis_tool", f'{date.today()}')
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)

        # loop over the list of sql tables and read them into pandas dataframe
        for f in read_table_names:
            df = pd.read_sql(f'SELECT * FROM {f}', con=db)
            # Creating a dict consisting of all dataframes
            if df.size != 0:
                dataframes_dict[f] = df  
            # Applying methods to dataframes defined on analysis_dict.py file
            for key,value in dat.analysis_dict().items():
                if df.size != 0:
                    vars()[key] = value(df)
                    dat.save_dataframe_excel(vars(),f"analysis_{f}_{date.today()}")
                else:
                    dat.save_dataframe_excel(df,f"analysis_{f}_{date.today()}")
        return dataframes_dict


    def multiple_dataset_apply_containing_cols_mysql(self):
        '''Detects columns that contains each other on entire database and saves as output file'''
        # Frames empty list to be used in further pandas dataframe creation operation
        frames = []
        # Getting all dataframes from another method of class
        # dataframes_dict = self.multiple_dataset_apply_mysql(self.host, self.user, self.password, self.database)
        dataframes_dict = self.multiple_dataset_apply_mysql()
        # Containing columns operation
        for key,value in dataframes_dict.items():
            for key_col,columnData in value.items():
                for key_1,value_1 in dataframes_dict.items():
                    for key_col_1,colondata in value_1.items():
                        if columnData.isin(colondata).all() == True and key_col == key_col_1 and key != key_1: # and "id" not in key_col and "Id" not in key_col_1
                            d = {"table_1" : [key], "col_1" : [key_col], "table_2" : [key_1], "col_2" : [key_col_1]}
                            df_output = pd.DataFrame(data=d)
                            frames.append(df_output)
                            global df_ultimate
                            df_ultimate = pd.concat(frames)
        # Creating working directory for daily partitioning of output files
        dir = os.path.join("C:\\", "Users\Lenovo\Desktop\exam_eti\containerized_tool\data_analysis_tool", f'{date.today()}')
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)
        # Writing to xlsx file
        writer = pd.ExcelWriter(f"containing_cols_{date.today()}.xlsx", engine="xlsxwriter")
        df_ultimate.to_excel(writer,sheet_name="containing_cols")
        writer.close()
        return "output files saved for containing columns"
    
    def find_value_mysql(self,value:str):
        ''' This function reads multiple tables from connected database 
        then find values searched in database tables saves into an xlxs'''
        # mysql connection cursor
        db=mysql.connector.connect(host = str(self.host), user = str(self.user), password = str(self.password), database = str(self.database))
        cursor=db.cursor()
        cursor.execute("SHOW TABLES")
        myresult = cursor.fetchall()
        # saving all tables of database into a list
        read_table_names = [table_name[0] for table_name in myresult]
        # Creating an empty list to fill pandas dataframe in further steps
        # global frames
        frames = []
        # Loop on all tables
        for f in read_table_names:
            # Reading sql tables into pandas dataframe
            df = pd.read_sql(f'SELECT * FROM {f}', con=db)
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
        # Saving output dataframe 
        writer = pd.ExcelWriter(f"find_value_{value}_{date.today()}.xlsx", engine="xlsxwriter")
        df_output = pd.DataFrame(frames)
        df_output.to_excel(writer,sheet_name="found_value")
        writer.close()
        return "value find table saved"
    

    def multiple_dataset_apply_mysql_query(self,sql_command:str):
        ''' This function gets sql statement as text input and runs it through connected 
         MYSQL db '''
        # Creating connection string and running sql command
        db=mysql.connector.connect(host = str(self.host), user = str(self.user), password = str(self.password), database = str(self.database))
        cursor=db.cursor()
        cursor.execute(f"{sql_command}")
        myresult = cursor.fetchall()
        return myresult
    
print("working")