from datetime import date
import sys
sys.path.insert(0, 'C:/Users/Lenovo/Desktop/exam_eti/containerized_tool/data_analysis_tool/src')
import dat

print("davar")

df = dat.df_read_aws('merkle-de-interview-case-study/de', 'item.csv')

functions_df_names = dat.analysis_dict()

for key, value in functions_df_names.items():
    # Creating dataframes defined on analysis_dict.py file
    vars()[key] = value(df)

dat.save_dataframe_excel(globals(), f"analysis_dataset_{date.today()}")
