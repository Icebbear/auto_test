# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      read_ini.py
# Author:       ice bear
# Datetime:     2023/12/13 15:34
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import configparser
import os.path


class ReadIni:
    def __init__(self):
        self.data_config = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_config")
        self.ini_path = os.path.join(self.data_config, "config.ini")

        self.conf = configparser.ConfigParser()
        self.conf.read(self.ini_path, encoding="utf-8")

    def get_file_path(self, key):
        return os.path.join(self.data_config, self.conf.get("file", key))

    def get_url(self, key):
        return self.conf.get("url" ,key)

    def get_sql_message(self, key):
        return self.conf.get("sql", key)

    def get_report_path(self, key):
        report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
        return os.path.join(report_path, self.conf.get("report", key))

    def get_test_path(self, key):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), self.conf.get("case_path", key))


if __name__ == '__main__':
    re = ReadIni()
    print(re.get_file_path("yaml"))
    # print(re.ini_path)
