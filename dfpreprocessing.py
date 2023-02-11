import pandas as pd

class DfPreprocessing:

    def preprocess(df: pd.DataFrame) -> pd.DataFrame:
        step1_check_year =  None


    def _convert_datetime(df: pd.DataFrame):

        try:
            column_selection = DfPreprocessing._create_col_dict(df)
            usr_date_input = input("Which column numbers are datetime fields? If multiple, use a comma inbetween columns ")
        except:
            pass

    def _detect_year(df:pd.DataFrame):
        list(df.columns)

    def _create_col_dict(df: pd.DataFrame):
        col_names = list(df.columns)
        col_dict = {}
        for i, colname in enumerate(col_names):
            col_dict[i + 1] = colname
        return col_dict
    