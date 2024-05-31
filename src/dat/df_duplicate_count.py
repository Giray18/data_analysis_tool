import pandas as pd
import codecs

def df_duplicate_count(df: pd.DataFrame):
    ''' Returns duplicate rows count/qty on dataset'''
    # Byte array cols detected
    byte_value_col = [df[i].name for i in df.columns if "b'" in str(df[i].iloc[0]) or "{" in str(df[i].iloc[0])]
    # Converted bytearrays to string
    for col_n in byte_value_col:
        df[col_n] = df[col_n].apply(lambda x: str(x))
    # Counting duplicates and filtering them
    df_duplicate = df.groupby(df.columns.tolist(),as_index=False).size()
    df_duplicate = df_duplicate[df_duplicate['size'] > 1] 
    ## Method not in use (ex method) below
    # duplicate_numb = len(df)-len(df.drop_duplicates())
    # df_duplicate = pd.DataFrame([duplicate_numb],columns = ["duplicate_qty"])
    return df_duplicate

if __name__ == '__main__':
    df_duplicate_count()