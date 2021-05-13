import json
from pprint import pprint

class WorkWithJson():
    def __init__(self):
        self.path_json = './res/setting.json'

    def get_data(self):
        """ Получить настройки из json """        
        with open(self.path_json, "r", encoding='utf8') as read_file:
            date_json = json.load(read_file)
        return date_json
