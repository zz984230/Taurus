from configs.config import Config
from presenter.dash_app import *
from presenter.global_pt import GlobalPt
from usecase.kind.kind_uc import KindUc
from presenter.kind_pt import KindPt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        self.__global_pt = GlobalPt(self.__cfg.logo_file, self.__cfg.bg_file).set_global_layout().set_left_layout().render()
        self.__kind_uc = KindUc(KindPt(self.__global_pt.get_right_div(), self.__cfg.yirgacheffe_kind_pic_file))

    def start(self):
        self.__init()
        print("Good")
        self.__kind_uc.run()
        render()
        app.run_server(debug=True)


if __name__ == "__main__":
    fire.Fire(Program)
