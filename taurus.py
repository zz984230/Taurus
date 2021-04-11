from configs.config import Config
from presenter.dash_app import *
from presenter.global_pt import GlobalPt
from usecase.kind.kind_uc import KindUc
from presenter.kind_pt import KindPt
from usecase.score.score_uc import ScoreUc
from presenter.score_pt import ScorePt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        kind_pt = KindPt(self.__cfg.yirgacheffe_kind_pic_file)
        score_pt = ScorePt()
        self.__global_pt = GlobalPt(self.__cfg.logo_file, self.__cfg.bg_file, kind_pt, score_pt).set_global_layout().set_left_layout().render()
        self.__kind_uc = KindUc(kind_pt)
        self.__score_uc = ScoreUc(self.__cfg, score_pt)

    def start(self):
        self.__init()
        render()
        self.__kind_uc.run()
        self.__score_uc.run()
        app.run_server(debug=True)


if __name__ == "__main__":
    fire.Fire(Program)
