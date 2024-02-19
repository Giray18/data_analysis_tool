import pandas as pd
import numpy as np

def df_describe_non_num(df: pd.DataFrame):
    ''' Returns short/statistical summary of non-numerical columns'''
    describe_non_numerical = df.describe(exclude=[np.number])
    return describe_non_numerical

if __name__ == '__main__':
    df_describe_non_num()