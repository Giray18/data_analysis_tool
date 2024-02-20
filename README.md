# Data Analysis Tool
Purpose of this repository is to create a dynamic tool that is consisting of python and pandas scripts for auto data analysis of tabular datasets located on AWS and Azure storage.
By running code chunk on (https://github.com/Giray18/data_analysis_tool/blob/main/data_analysis_by_loop.ipynb) a xmlx formatted data analysis summary of source dataset being saved into working directory.

## Elements of Repository
**DAT Python Package** : A created python package holding methods that can make dynamic data analysis based on data types exist on dataset. Mentioned methods are defined below; (Package link : https://github.com/Giray18/data_analysis_tool/tree/main/dat)
  
  **analysis_dict.py** : A customizable dict generator that will put methods into dict. All data analysis activities will be done according to selected methods in dict

  **df_shape.py** : Returns a table that shows row and column count on the dataset
  ![picture alt](data_analysis_tool_output_screenshots/df_shape.PNG)  
  
  **df_col_types.py** : Returns a dataframe that defines datatypes of fields on dataset
  ![picture alt](data_analysis_tool_output_screenshots/df_col_types.PNG)
  
  **df_head.py** : Returns a dataframe shows first 5 rows of dataset for quick check of values in table  
  ![picture alt](data_analysis_tool_output_screenshots/df_head.PNG)

  **df_unique_cols.py** : Returns a dataframe shows field names that holds only unique values / No duplication
  
  **df_date_time.py** : Returns table consisting of date-time values holding fields, min date-time on mentioned column, max date-time on mentioned column, difference between min and max values on mentioned column
  ![picture alt](data_analysis_tool_output_screenshots/df_date_cols.PNG)
  
  **df_describe_all.py** : Returns table that is holding general stats regarding to all fields of dataset (e.g count, unique values count, top frequency value, (mean, std. min and ntiles for numeric columns))
  ![picture alt](data_analysis_tool_output_screenshots/df_describe_all.PNG)
  
  **df_describe_non_numerical.py** : Returns table that is holding general stats regarding to non numeric fields of dataset (e.g count, unique values count, top frequency value)
  ![picture alt](data_analysis_tool_output_screenshots/df_describe_non_num.PNG)

  **df_detect_json.py** : Returns table that holds names of JSON structured value holding fields<br>
  ![picture alt](data_analysis_tool_output_screenshots/df_json_cols.PNG)

  **df_detect_xml.py** : Returns table that holds names of XML structured value holding fields<br>
  ![picture alt](data_analysis_tool_output_screenshots/df_xml_cols.PNG)

  **df_duplicate_count.py** : Returns table that holds amount of duplicate rows in dataset<br>
  ![picture alt](data_analysis_tool_output_screenshots/df_duplicate_count.PNG)

  **df_flatten_json.py** : Returns table that flattens JSON structured value holding fields and merges them into main dataset

  **df_null_counts.py** : Returns table that shows count of null value holding rows per field and their percent to total row count per field.
  ![picture alt](data_analysis_tool_output_screenshots/df_null_count.PNG)

  **df_value_counts.py** : Returns table that shows value counts on a field that is more than %5 of entire field row amount.
  ![picture alt](data_analysis_tool_output_screenshots/df_value_counts.PNG)


  



  

  

