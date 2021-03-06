import eel
import os
import random
from backend import afd_docx
from backend import afd_ggl
from backend import afd_helps
from backend import afd_json
from backend import afd_pandas


class Main():
    def __init__(self):
        self.config = afd_json.WorkWithJson().get_data()
        # Получение таблицы из Гугл
        self.creds = afd_json.WorkWithJson().get_creds()
        self.ggl = afd_ggl.GoogleSheet(self.config, self.creds)
        self.help = afd_helps.HelpsMetods()

    def main(self, input_text):
        table = self.ggl.get_values(self.config['table_name'])
        # Обработка в pandas
        pd = afd_pandas.WorkWithPandas()
        df_vk = pd.create_df(
            date_df=table, row_name=self.config['row_tags']-1)
        list_rows = self.help.convet_text_in_numbers(input_text)
        return_text = []
        for row in list_rows:
            vk_dict = pd.convert_row_to_dict(df_vk, row)
            # pprint(vk_dict)
            # Заполнение шаблона
            doc = afd_docx.WorkWithDocx()
            return_text.append(doc.fill_docx(row, vk_dict))
        return return_text


if __name__ == '__main__':
    go = Main()
    eel.init('frontend')

    @eel.expose
    def pick_file(input_text):
        rows_namedoc = go.main(input_text)
        if input_text == '':
            return "<p><i>Введите номера строк</i></p>"
        else:
            return_text = '<caption>Вывод</caption><tr><th>Номер строки</th><th>Наименование</th></tr>'
            for row, name in rows_namedoc:
                # return_text += "<p>" + row + "</p>"
                return_text += "<tr><td>" + \
                    str(row) + "</td><td>" + name + "</td></tr>"
            return return_text

    eel.start('main.html', mode='chrome', size=(450, 450))
