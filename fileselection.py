from typing import Union
import os

class FileSelection:

    @staticmethod
    def validate_csv(target_dir: str) -> Union[list[str], None]:
        file_list = FileSelection.return_dir_file_list(target_dir)
        
        csv_list = []
        try:
            for item in file_list:
                if item[-4:] == '.csv':
                    csv_list.append(item)
                else:
                    continue
            return csv_list
        except:
            print('Error in validate_csv')

    @staticmethod
    def return_dir_file_list(target_dir: str) -> list[str]:
        source_dir = os.getcwd() + '/' + target_dir
        try:
            file_list = os.listdir(source_dir)
            return file_list
        except:
            print('File directory does not exist')

    
    @staticmethod
    def view_csv_files(csvkp: dict):
        for key in csvkp:
            print(f'{key} | {csvkp[key]}')
        return None

    @staticmethod
    def create_csv_dict(csv_list: list[str]) -> dict:
        csvkp = {}
        csvkp[0] = 'Exit'
        for i, file in enumerate(csv_list):
            csvkp[i+1] = file
        return csvkp

    @staticmethod
    def return_target(csv_dict: dict) -> str:
        while True:
            try:
                user_selection = int(input('CSV number to analyze: '))
                if user_selection == 0:
                    print('Exiting File Selection...')
                    break
                else:
                    return csv_dict[user_selection]
            except:
                print('An invalid option was selected. Try again or exit by entering "0"')