import json
from cryptography.fernet import Fernet

class WorkWithJson():
    def __init__(self):
        self.path_json = './res/setting.json'

    def get_data(self):
        
        """ Получить настройки из json """        
        with open(self.path_json, "r", encoding='utf8') as read_file:
            date_json = json.load(read_file)
        return date_json

    def get_creds(self):
        key = "Bkl93e2_LInKwSBlxe8vyZck5bZc6OWjdIBDLV_XLa4="
        with open('./res/creds.json', 'rb') as f:
            data = f.read()
        decrypt_file = Fernet(key).decrypt(data)
        creds_json = json.loads(decrypt_file)
        return creds_json



