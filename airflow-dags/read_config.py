from constant import Constant
import configparser
import os

class Config:
    #Read config file
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    ini_file_path = os.path.join(BASE_DIR, Constant.INI_FILE_PATH)

    config = configparser.ConfigParser()
    config.read(ini_file_path)
    stage = config.get(Constant.DEFINITION, Constant.STAGE)