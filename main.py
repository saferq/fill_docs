# import os
from pprint import pprint
from backend import afd_json, afd_ggl, afd_pandas, afd_docx, afd_helps


class Main():
    def __init__(self):
        # os.system("mode con cols=80 lines=30")
        print("0 - для выхода")
        # Получение конфигурации из json файла
        self.config = afd_json.WorkWithJson().get_data()
        # Получение таблицы из Гугл
        self.ggl = afd_ggl.GoogleSheet(self.config)
        self.help = afd_helps.HelpsMetods()

    def main(self):
        while True:
            print("""\nВвести номера строк:""")
            a = input("")
            if a == '0':
                # os.system("cls")
                break
            # Загрузка таблицы
            table = self.ggl.get_values(self.config['table_name'])
            # Обработка в pandas
            pd = afd_pandas.WorkWithPandas()
            df_vk = pd.create_df(date_df=table, row_name=self.config['row_tags']-1)
            if a == 'help':
                print('''\nПомощь в программе \nтаки так \nи вот так вот''')
            else:
                list_rows = self.help.convet_text_in_numbers(a)
                for row in list_rows:
                    vk_dict = pd.convert_row_to_dict(df_vk, row)
                    # pprint(vk_dict)
                    # Заполнение шаблона
                    doc = afd_docx.WorkWithDocx()
                    doc.fill_docx(row, vk_dict)


if __name__ == '__main__':
    go = Main()
    go.main()
