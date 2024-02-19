import pandas as pd

def df_duplicate_count(df: pd.DataFrame):
    ''' Returns duplicate rows count/qty on dataset'''
    duplicate_numb = len(df)-len(df.drop_duplicates())
    df_duplicate = pd.DataFrame([duplicate_numb],columns = ["duplicate_qty"])
    return df_duplicate

if __name__ == '__main__':
    df_duplicate_count()