import pandas as pd
import os
import glob
import numpy as np
import re

# # use glob to get all the csv files 
# # in the folder
# path = os.getcwd()
# csv_files = glob.glob(os.path.join(path, "*.csv"))

# #xlsx location
# xlsx_files = glob.glob(os.path.join(path, "*.xlsx"))

# # loop over the list of csv files
# e = pd.DataFrame()
# for f in csv_files:
      
#     # read the csv file
#     df = pd.read_csv(f, low_memory=False)
#     e = pd.concat([e,df])

#     File_name =  f.split("\\")[-1]
# # d = []
# # counter = 0
# for (columnName, columnData) in e.items():
#     for i in range(len(columnName)):
#         if columnData.isin(e.iloc[:,i]).all()  == True and columnData.dropna().empty == False:
#             print(columnName,e.iloc[:,i].name)

def detect_containing_columns(df: pd.DataFrame):
    df = df.astype('str')

    alldfs = [var for var in dir() if isinstance(eval(var), pd.core.frame.DataFrame)]
    dataframes_dict = {}
    for df in alldfs:
        dataframes_dict[df] = vars()[df]

    frames = []
    for a in range(len(alldfs)):
        for (columnName, columnData) in vars()[alldfs[a]].items():
            pass
        for key,colondata in dataframes_dict.items():
            pass
            for (colonname, colondata) in colondata.items():
                if columnData.isin(colondata).all() == True and columnName != colonname:
                    list_1 = [columnName,colonname,[alldfs[a]],key]
                    # print(columnName,colonname,[alldfs[a]],key)
                    df_output = pd.DataFrame([list_1],columns = "columns_containing")
    return df_output
