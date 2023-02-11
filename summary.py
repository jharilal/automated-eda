import pandas as pd
from prettytable import PrettyTable

class Summary:

    def overview(df: pd.DataFrame):
        # Total Count /Total Attributes / Total Null
        overview = PrettyTable()
        overview.field_names = ['Total Attributes', 'Total Observations', 'Total Null Values']
        overview.add_row([Summary._total_col_num(df),
                          Summary._total_obs_count(df),
                          Summary._total_null_count(df)])
        return overview

    def attribute_summary(df: pd.DataFrame):
        attribute_table = PrettyTable()
        attribute_table.field_names = ['ID', 'Column Name', 'Column Type', 'Total Count', 'Total Null', 'Null %']
        attribute_table.add_rows(Summary._create_attribute_summary(df))
        return attribute_table

    
    def _create_attribute_summary(df: pd.DataFrame):
        rows = []
        for i, col in enumerate(df.columns):
            
            totcount, nullsum = df[col].count(), df[col].isnull().sum(),

            rows.append([
                i, 
                col, 
                df[col].dtypes, 
                totcount,
                nullsum,
                round(nullsum / totcount, 4) * 100
            ])
        return rows

    def _total_col_num(df: pd.DataFrame) -> int:
        return len(df.columns)

    def _total_obs_count(df: pd.DataFrame) -> int:
        return df.shape[0]
    
    def _total_null_count(df: pd.DataFrame) -> int:
        return df.isnull().sum().sum()
    