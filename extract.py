import pandas as pd
import os
import time


from fileselection import FileSelection


class Extract:
    
    @staticmethod
    def extractor(target_dir: str) -> pd.DataFrame:
        target_csv_path = Extract.select_target(target_dir)
        if target_csv_path == None:
            return None
        return Extract.read(target_csv_path)



    @staticmethod
    def read(file_path):
        try:
            df = pd.read_csv(file_path, header=0)
            return df
        except:
            print(file_path)
            if file_path == None:
                print(f'file_path = {file_path}')
                print('Exiting...')
                time.sleep(2)
                return None
            print('Could not read csv - check file to confirm error')
    
    @staticmethod
    def select_target(target_dir: str):
        csv_list = FileSelection.validate_csv(target_dir)
        csv_dict = FileSelection.create_csv_dict(csv_list)
        FileSelection.view_csv_files(csv_dict)
        
        try:
            target_csv_path = os.path.abspath(target_dir) + '/' + FileSelection.return_target(csv_dict)
            print(f'...{target_csv_path}')
            return target_csv_path
        except:
            'Exiting extraction...'
            time.sleep(0)