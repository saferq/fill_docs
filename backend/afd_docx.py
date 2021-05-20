from pprint import pprint
from docxtpl import DocxTemplate
from colorama import init, Fore, Back, Style
init()


class WorkWithDocx():
    def __init__(self):
        pass

    def fill_docx(self, row, context, name_file='name', template_file='template'):
        """  Заполнение шаблона """
        try:
            doc = DocxTemplate(f'res/{context[template_file]}')
            doc.render(context)
            name_file = self.format_name_file(context[name_file])
            print(f"{Back.GREEN}{Fore.BLACK}{row}: {name_file}{Style.RESET_ALL}")
            doc.save(name_file + '.docx')
            return [row, name_file]
        except:
            print(
                f'{Back.RED}{Fore.BLACK}{row}: Ошибка. В папке "res" нет файла шаблона {context[template_file]}{Style.RESET_ALL}')
            # return f'Ошибка. В папке "res" нет файла шаблона {context[template_file]}'
            return [row, f'Ошибка. В папке "res" нет файла шаблона {context[template_file]}']

    def format_name_file(self, text, length_name=35):
        """ 
        Функция форматирования имени файла убирает 
        нечитаемые символы и ограничивает длину текста
         """
        dictionary_work = {
            # 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            # 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
            # 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            # 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '',
            # 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'u', 'я': 'ja',
            # 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
            # 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
            # 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            # 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '',
            # 'Ы': 'y', 'Ь': '', 'Э': 'E', 'Ю': 'U', 'Я': 'YA',
            'ґ': 'r', 'ї': 'r', 'є': 'e', 'Ґ': 'g', 'Ї': 'i', 'Є': 'e',
            ',': '_', '.': '_', '?': '',
            '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '',
            '~': '', '!': '', '@': '', '*': '', ':': '',
            '№': '#', ' ': '_', '—': '-'
        }
        for key in dictionary_work:
            text = text.replace(key, dictionary_work[key])
        text = text.replace('__', '_')
        text = text.replace('__', '_')
        if text[length_name-1:length_name] == '_':
            return text[0:length_name-1]
        else:
            return text[0:length_name]


if __name__ == '__main__':
    wd = WorkWithDocx()
