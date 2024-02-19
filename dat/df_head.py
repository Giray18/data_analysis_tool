import pandas as pd

def df_head(df: pd.DataFrame,line_number = 0):
    ''' Returns first lines of a dataframe
    for quick look of table field values'''
    df = df.head(line_number)
    return df

if __name__ == '__main__':
    df_head()
