import pandas as pd

from summary import Summary


class Analyze:

    @staticmethod
    def analyzer(df: pd.DataFrame):
        if Analyze._validate_df(df):
            return None
        Analyze.dataframe_summary(df)
    
    
    @staticmethod
    def dataframe_summary(df: pd.DataFrame) -> None:
        
        # Source File

        # Overview Table
        print(Summary.overview(df))
        print(Summary.attribute_summary(df))

        pass

    def attribute_names(df: pd.DataFrame) -> list:
        print(df.columns)

    def attribute_types(df: pd.DataFrame) -> str:
        print()

    def _validate_df(df: pd.DataFrame):
        return type(df) != pd.DataFrame