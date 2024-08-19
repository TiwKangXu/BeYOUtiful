from datetime import datetime

class Utils:
    @staticmethod
    def get_datetime_string():
        return datetime.now().strftime("%d%m%Y_%H%M%S")

    @staticmethod
    def parse_json_dir_path(folder):
        return '/Users/tiwkangxu/Desktop/NOC2024/Hackathon/BeYOUtiful/jsons/' + folder
    
    @staticmethod
    def print_dic(dic):
        for key, value in dic.items():
            print(f"{key}: {value}")
