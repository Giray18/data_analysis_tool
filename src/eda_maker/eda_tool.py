import sys
sys.path.insert(
    0, 'C:/Users/Lenovo/Desktop/exam_eti/containerized_tool/data_analysis_tool/src')
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
import dat
import mysql.connector
import mysql_analyzer
from collections import defaultdict
from mysql.connector.errors import Error
from mysql.connector import errorcode
import json
import re
import os
from datetime import datetime, timedelta, date
from dataclasses import dataclass, field


# import mysql.connector.errors as err


@dataclass
class EdaHelper:
    '''Class to apply exploratory data analysis activities to datasets'''
    host: str
    user: str
    password: str
    database: str
    db: str = field(init=False)

    def __post_init__(self) -> None:
        # Creating connection string
        try:
            self.db = mysql.connector.connect(host=str(self.host), user=str(
                self.user), password=str(self.password), database=str(self.database))
        except mysql.connector.ProgrammingError as e:
            raise ValueError('Wrong database name') from e
        except mysql.connector.DatabaseError as err:
            raise ValueError('Wrong server name') from err

    def sql_query(self, sql_command: str = None) -> list:
        '''Running SQL command passed to function and fetch all brings results'''
        cursor = self.db.cursor()
        cursor.execute(sql_command)
        res = cursor.fetchall()
        cursor.close()
        return res

    def sql_query_to_pandas(self, sql_command: str = None) -> pd.DataFrame:
        '''Running SQL command parsing query results saving into dataframe'''
        df = pd.read_sql_query(f'{sql_command}', con=self.db)
        return df

    def filter_numeric_cols(self, sql_command: str = None) -> list:
        '''Returns numeric columns of dataframe into a list'''
        num_cols = list(pd.read_sql_query(
            f'{sql_command}', con=self.db)._get_numeric_data().columns)
        return num_cols

    def filter_categorical_cols(self, sql_command: str = None) -> list:
        '''Returns categorical columns of dataframe into a list'''
        df_cols = list(self.sql_query_to_pandas(f'{sql_command}').columns)
        cat_cols = [
            x for x in df_cols if x not in self.filter_numeric_cols(f'{sql_command}')]
        return cat_cols

    def desc_uni_num_feature(self, feature_name: str = None, sql_command: str = None, bins:  int = 30, edgecolor: str = 'k', **kwargs) -> list:
        '''Returns matplotlib graph of selected columns hist dist. and describe values'''
        fig, ax = plt.subplots(figsize=(8, 4))
        df = pd.read_sql_query(
            f'{sql_command}', con=self.db)[feature_name].hist(bins=bins, edgecolor=edgecolor, ax=ax, **kwargs)
        ax.set_title(feature_name, size=15)
        plt.figtext(1.15, 0.15, pd.read_sql_query(
            f'{sql_command}', con=self.db)[feature_name].describe().round(2), size=17)

    def desc_uni_cat_feature(self, feature_name: str = None, sql_command: str = None) -> list:
        count = pd.read_sql_query(
            f'{sql_command}', con=self.db)[feature_name].value_counts()
        percent = 100*pd.read_sql_query(
            f'{sql_command}', con=self.db)[feature_name].value_counts(normalize=True)
        df = pd.DataFrame({'count':count, 'percent':percent.round(1)})
        return df