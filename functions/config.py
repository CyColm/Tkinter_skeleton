# -*- coding: utf-8 -*-

from configobj import ConfigObj
import os
from pathlib import Path


class Config:
    def __init__(self,
                 path=str(Path(__file__).parent.parent)+os.sep+"settup.ini"):
        self.config = ConfigObj(path)

    def get(self, section, option, type):
        try:
            if type == 'str':
                return True, self.config[section][option]
            elif type == 'int':
                return True, self.config[section].as_int(option)
            elif type == 'bool':
                return True, self.config[section].as_bool(option)
        except Exception:
            return False, None


if __name__ == '__main__':
    Config()
