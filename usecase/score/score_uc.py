from repository.score_repo import ScoreSheet
import pandas as pd


class ScoreUc(object):
    def __init__(self, cfg, prt):
        self.__repo = ScoreSheet(cfg.yirgacheffe_score_path).load()
        self.__prt = prt
        self.__df = pd.DataFrame()
        self.__cols = list()

    def __get_data(self):
        self.__df = self.__repo.get_data()
        self.__cols = self.__repo.get_column()

    def __deal_data(self):
        pass

    def run(self):
        self.__get_data()
        self.__deal_data()
        self.__prt.render(self.__df, self.__cols)
