import pandas as pd
import dat
# from df_flatten_json import *
# from df_head import *
# from df_col_types import *
# from df_shape import *
# from df_describe_non_num import *
# from df_duplicate_count import *
# from df_unique_cols import *
# from df_null_counts import *
# from df_detect_json import *
# from df_detect_xml import *
# from df_date_time import *
# from df_value_counts import *



def analysis_dict():
    ''' Returns a dict consisting of dataframe names and dat package functions'''
    analysis_dict = {"df": dat.df_flatten_json,"head": dat.df_head , 
                     "col_types" : dat.df_col_types, "shape" :dat.df_shape,
                     "describe_non_num" : dat.df_describe_non_num, "duplicate_count" : dat.df_duplicate_count,
                     "unique_cols" : dat.df_unique_cols, "null_counts" : dat.df_null_counts,
                     "json_cols" : dat.df_detect_json, "xml_cols" : dat.df_detect_xml,
                     "date_cols" :dat.df_date_time, "value_counts" : dat.df_value_counts}

    # analysis_dict = {"df": df_flatten_json,"head": df_head , 
    #                  "col_types" : df_col_types, "shape" :df_shape,
    #                  "describe_non_num" : df_describe_non_num, "duplicate_count" : df_duplicate_count,
    #                  "unique_cols" : df_unique_cols, "null_counts" : df_null_counts,
    #                  "json_cols" : df_detect_json, "xml_cols" : df_detect_xml,
    #                  "date_cols" :df_date_time, "value_counts" : df_value_counts}

    return analysis_dict

if __name__ == '__main__':
    analysis_dict()