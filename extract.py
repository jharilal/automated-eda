import pandas as pd

class Extract:
    
    def read(source_file_path):
        try:
            df = pd.read_csv(source_file_path)
        except:
            print('Could not read csv')