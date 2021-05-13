import pandas as pd


class WorkWithPandas():
    def create_df(self, date_df, row_name=0, row_content=1):
        """ Создание DataFrame """
        df = pd.DataFrame(date_df[row_content:], columns=date_df[row_name])
        return df

    def convert_row_to_dict(self, df, row, correct_row=2):
        dict_row = df.iloc[row-correct_row].to_dict()
        return dict_row