# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      read_ini.py
# Author:       xxxxxxx
# Datetime:     2023/12/2 11:22
# Description:
# 
# ---------------------------------------------------------------------------
import configparser
import os


class ReadIni:
    def __init__(self):
        self.data_config = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_config")
        ini_path = os.path.join(self.data_config, "config.ini")

        self.conf = configparser.ConfigParser()
        self.conf.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        return os.path.join(self.data_config, self.conf.get("file", key))

    def get_url(self, key):
        return self.conf.get("url", key)

    def get_sql_message(self, key):
        return self.conf.get("sql", key)

    def get_report_path(self, key):
        report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
        return os.path.join(report_path, self.conf.get("report", key))

    def get_test_path(self, key):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), self.conf.get("case_path", key))


if __name__ == '__main__':
    read_ini = ReadIni()
    # D:\Document\PythonDoc\test_57_unittest\WebAutoTest\test_case
    # D:\Document\PythonDoc\test_57_unittest\WebAutoTest\test_case
    print(read_ini.get_test_path("test_case"))
