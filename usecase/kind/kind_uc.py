from repository.kind_repo import KindSheet
import pandas as pd


class KindUc(object):
    def __init__(self, prt):
        self.__prt = prt
        self.__df = pd.DataFrame(dict(score=[4, 1, 4, 4, 1], label=['酸度: Acidity', '苦度: Bitterness', '风味: Flavor', '甜度: Sweetness', '醇厚度: Body']))
        self.__cols = list()

    def run(self):
        self.__prt.render(self.__df)
