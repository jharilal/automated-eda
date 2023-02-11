import pandas as pd
from fileselection import FileSelection
import os

class Extract:
    
    @staticmethod
    def read(file_path):
        try:
            df = pd.read_csv(file_path, header=0)
            return df
        except:
            print('Could not read csv - check file to confirm error')
    
    @staticmethod
    def select_target(target_dir: str):
        csv_list = FileSelection.validate_csv(target_dir)
        csv_dict = FileSelection.create_csv_dict(csv_list)
        FileSelection.view_csv_files(csv_dict)
        try:
            target_csv = os.path.abspath(target_dir) + '/' + FileSelection.return_target(csv_dict)
            print(f'...{target_csv}')
            return target_csv
        except:
            'Exiting extraction...'

