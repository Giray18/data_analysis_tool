import pandas as pd
import re

def df_date_time(df: pd.DataFrame):
    ''' Returns a dataframe consisting of field names 
    that date time format and second dataframe shows min, max and 
    datediff between min and max'''
    #Regex pattern for date columns
    pattern_d = re.compile(r"[0-9]{4}.[0-9]{2}.[0-9]{2}.*", re.IGNORECASE)
    pattern_d_alt = re.compile(r"[0-9]{2}.[0-9]{2}.[0-9]{4}.*", re.IGNORECASE)
    #Loop through columns detect date columns
    col_date = [df[i].name for i in df.columns if pattern_d.match(str(df[i].iloc[0])) or pattern_d_alt.match(str(df[i].iloc[0]))]
    df_date_cols = pd.DataFrame(col_date,columns = ["col_date"])
    # Getting min and max timestamps from dataset`s timestamp column
    if int(df_date_cols.size) > 0:
        min_max_date = [df[i].min() for i in df_date_cols.col_date.values]
        min_max_date.extend([df[i].max() for i in df_date_cols.col_date.values])
    df_date_min_max = pd.DataFrame([min_max_date],columns = ["min_date","max_date"])
    # Converting related columns to date-time datatype
    for i in df_date_min_max.columns:
        df_date_min_max[i] = pd.to_datetime(df_date_min_max[i], format='mixed')
    # Adding diff dates column
    df_date_min_max = df_date_min_max.assign(diff_dates=df_date_min_max['max_date']-df_date_min_max['min_date'])
    # Concat all columns into one
    frames = [df_date_cols,df_date_min_max]
    df_ultimate = pd.concat(frames)
    return df_ultimate


if __name__ == '__main__':
    df_date_time()