import pandas as pd


class ScoreSheet(object):
    def __init__(self, src_data_file):
        self.__src_path = src_data_file
        self.__df = pd.DataFrame()
        self.__cols = list()

    def __transform(self):
        self.__cols = self.__df.columns
        self.__df[self.__cols[1:]] = self.__df[self.__cols[1:]].astype('float')

    def load(self):
        self.__df = pd.read_csv(self.__src_path, encoding='gbk')
        self.__transform()
        return self

    def get_data(self, col_name=None):
        if col_name is None:
            return self.__df

        return self.__df[col_name]

    def get_column(self) -> list:
        return list(self.__cols)
