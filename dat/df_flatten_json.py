import pandas as pd
import json

def df_flatten_json(df: pd.DataFrame):
    ''' Flattenning JSON column and concating it to original 
    df dataframe '''
    col_with_json_val = [df[i].name for i in df.columns if "{" in str(df[i].iloc[0]) and ":" in str(df[i].iloc[0])]
    df_json_cols = pd.DataFrame(col_with_json_val,columns = ["col_with_json_val"])
    if int(df_json_cols.size) > 0:
        for i in df_json_cols.col_with_json_val.values:
            # Coming from a past problem can be deleted
            if i == "Column1":
                continue
            else:                                                                                                                                     
                vars()[i] = df[i].map(lambda x: json.loads(x))
                vars()[i] = pd.json_normalize(vars()[i])
                df = df.join(vars()[i])
    else:
        df
    return df


if __name__ == '__main__':
    df_flatten_json()