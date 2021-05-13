import re

class HelpsMetods():
    
    def convet_text_in_numbers(self, text):
        """ Текст полный текст """
        # Замена символов
        text = re.sub(r' ', '', text)
        text = re.sub(r'[.]', ',', text)
        list_text = re.split(r',', text)
        list_numbers = []
        for n in list_text:
            if re.fullmatch(r'\d+', n) != None:
                list_numbers.append(int(n))
            elif re.fullmatch(r'\d+-\d+', n) != None:
                nn = re.split(r'-', n)
                nn = [int(x) for x in nn]
                n_min = min(nn)
                n_max = max(nn)
                n_list = list(range(n_min, n_max + 1))
                list_numbers = list_numbers + n_list
            else:
                pass
        numbers = sorted(set(list_numbers))
        return numbers