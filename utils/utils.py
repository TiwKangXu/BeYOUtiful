from datetime import datetime

from constants import BEYOUTIFUL_PATH

class Utils:
    @staticmethod
    def get_datetime_string():
        return datetime.now().strftime("%d%m%Y_%H%M%S")

    @staticmethod
    def parse_json_dir_path(folder):
        return BEYOUTIFUL_PATH + '/jsons/' + folder
    
    @staticmethod
    def print_dic(dic):
        for key, value in dic.items():
            print(f"{key}: {value}")
