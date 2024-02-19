import pandas as pd

class analysis:

    def __init__(self,df: pd.DataFrame):
        self.df = df
        # self.number = number

    def df_col_types(self):
        col_types = self.df.dtypes
        df_col_types = pd.DataFrame([col_types.values],columns=[self.df.columns])
        return df_col_types
    
