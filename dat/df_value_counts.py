import pandas as pd
import numpy as np

def df_value_counts(df: pd.DataFrame):
    ''' Returns dataframe that shows field values that takes 
    more than %5 of total values on a field'''
    #Created an empty dict to append series for out concat operation
    dict_1 = {}
    for i in df.columns:
        if df[i].dtype in ["string","object"]:
            s = df[i].explode().value_counts(normalize=True)
            # Filtered values does not have more than %5 of all values in a particular column
            s = s.loc[lambda x : x >= 0.05]
            dict_1[i] = []
            dict_1.update({i:s})
            # Concat all series we created into one
            df_ultimate = pd.concat(dict_1, axis = 1)
            # Removed all null columns
            df_ultimate = df_ultimate.loc[:,df_ultimate.notna().any(axis=0)]
            df_ultimate = df_ultimate.astype(float).map('{:,.1%}'.format)
    return df_ultimate

if __name__ == '__main__':
    df_value_counts()