import pandas as pd
import dat

def analysis_dict():
    ''' Returns a dict consisting of dataframe names and dat package functions'''
    analysis_dict = {"df": dat.df_flatten_json,"df_head": dat.df_head , 
                     "df_col_types" : dat.df_col_types}

    return analysis_dict

if __name__ == '__main__':
    analysis_dict()