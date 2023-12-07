# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   AutoTest
# FileName:      read_ini.py
# Author:       zdq
# Datetime:     2023/12/4 10:51
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import configparser
import os.path

from config.settings import *


class ReadIni:
    def __init__(self):
        self.data_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
        ini_path = os.path.join(self.data_config_path, "config.ini")

        self.conf = configparser.ConfigParser()
        self.conf.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        try:
            file_name = self.conf.get(FILE, key)
        except:
            raise KeyError("输入file节点下的key错误，请检查配置文件")
        file_path = os.path.join(self.data_config_path, file_name)

        if os.path.isfile(file_path):
            return file_path
        else:
            raise KeyError("获取file节点下文件路径错误，请检查配置文件")

    def get_host(self, key):
        return self.conf.get(URL_HOST, key)

    def get_table_name(self, key):
        return self.conf.get(TABLE, key)

    def get_sql(self, key):
        return self.conf.get(CONN_SQL, key)


if __name__ == '__main__':
    re = ReadIni()
    x = re.get_file_path("sql")
    print(x)
