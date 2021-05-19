# -*- coding: utf-8 -*-
import pprint as pp
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet():
    """ Работа с google таблицей """

    def __init__(self, config, creds):
        d_json = creds
        self.table_key = config['table_key']

    def get_values(self, sheet_name):
        """ 
        Получить данные таблицы     
        sheet_name - Имя вкладки таблицы
         """
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
        credentails = ServiceAccountCredentials.from_json_keyfile_dict(
            self.cred_json, scope)
        client = gspread.authorize(credentails)
        sh = client.open_by_key(self.table_key)
        ws_table = sh.worksheet(sheet_name)
        data_sheet = ws_table.get_all_values()
        return data_sheet


if __name__ == '__main__':
    pass
