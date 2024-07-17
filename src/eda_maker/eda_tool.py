import sys
sys.path.insert(0, 'C:/Users/Lenovo/Desktop/exam_eti/containerized_tool/data_analysis_tool/src')
import numpy as np
import pandas as pd
import dat
import mysql.connector
import mysql_analyzer
from collections import defaultdict
import json
import re
import os
from datetime import datetime, timedelta, date
from dataclasses import dataclass, field

@dataclass
class EdaHelper:
    '''Class to apply exploratory data analysis activities to datasets'''
    host : str
    user : str
    password : str
    database : str
    db : str = field(init=False)

    def __post_init__(self):
        # Creating connection string
        self.db=mysql.connector.connect(host = str(self.host), user = str(self.user), password = str(self.password), database = str(self.database))

    def sql_command(self,sql_command : str = None):
        '''Runnint SQL command passed to function and fetch all brings results'''
        cursor=self.db.cursor()
        cursor.execute(sql_command)
        # myresult = cursor.fetchall()
        return cursor.fetchall()
