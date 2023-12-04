# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      read_ini.py
# Author:       xxxxxxx
# Datetime:     2023/11/3 14:05
# Description:
# 
# ---------------------------------------------------------------------------
import configparser
import os
from InterfaceAutoTest_v3.common import log
from InterfaceAutoTest_v3.data_config.settings import *


class ReadIni:
    def __init__(self):
        """读取ini文件"""
        self.data_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_config")
        ini_path = os.path.join(self.data_config_path, "config.ini")

        self.conf = configparser.ConfigParser()
        self.conf.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        """根据key，获取file节点下文件的路径"""
        try:
            file_name = self.conf.get(FILE, key)
        except:
            log.error("输入file节点下的key，错误，请求察看配置文件~！！！")
            raise KeyError("输入file节点下的key，错误，请求察看配置文件~！！！")

        file_path = os.path.join(self.data_config_path, file_name)

        if os.path.isfile(file_path):
            return file_path
        else:
            log.error("获取file节点下，文件的路径错误，请察看配置文件是否配置正确~！！！")
            raise FileExistsError("获取file节点下，文件的路径错误，请察看配置文件是否配置正确~！！！")

    def get_host(self, key):
        """根据key，获取域名"""
        try:
            return self.conf.get(URL_HOST, key)
        except:
            log.error("输入host节点下的key，错误，请求察看配置文件~！！！")
            raise KeyError("输入host节点下的key，错误，请求察看配置文件~！！！")

    def get_table_name(self, key):
        """根据key，获取工作表名称"""
        try:
            return self.conf.get(TABLE, key)
        except:
            log.error("输入table节点下的key，错误，请求察看配置文件~！！！")
            raise KeyError("输入table节点下的key，错误，请求察看配置文件~！！！")

    def get_sql_message(self, key):
        """根据key，获取数据库"""
        try:
            return self.conf.get(CONN_SQL, key)
        except:
            log.error("输入sql节点下的key，错误，请求察看配置文件~！！！")
            raise KeyError("输入sql节点下的key，错误，请求察看配置文件~！！！")


if __name__ == '__main__':
    ini = ReadIni()
    print(ini.get_sql_message("host"))
