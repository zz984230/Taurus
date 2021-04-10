import os
import toml
from utils.util import Util

_ETC_DIR = os.path.join(Util.get_root_path(), 'etc')


class Config(object):
    def __init__(self):
        self.__etc_file = os.path.join(_ETC_DIR, 'cafe.toml')
        self.__logo_file = None
        self.__bg_file = None
        self.__data = None

    def init(self):
        try:
            with open(self.__etc_file, 'r') as f:
                self.__data = toml.load(f)
                self.__logo_file = self.__data["icon"]["logo_file"]
                self.__bg_file = self.__data["icon"]["bg_file"]
        except IOError as e:
            raise e

    @property
    def logo_file(self):
        return self.__logo_file

    @property
    def bg_file(self):
        return self.__bg_file

    @property
    def yirgacheffe_kind_data_file(self):
        return self.__data["report"]["yirgacheffe_kind_path"]

    @property
    def yirgacheffe_kind_pic_file(self):
        return self.__data["kind"]["yirgacheffe"]
