# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      login_page.py
# Author:       zdq
# Datetime:     2023/12/14 10:29
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import time

from basic.basic import Basic
from common.read_ini import ReadIni
from common.read_yaml import read_yaml


class LoginPage(Basic):
    yaml_data = read_yaml(ReadIni().get_file_path("yaml"))

    def login(self, username, password):
        self.send_keys(self.yaml_data["loginPage"]["username"], username)
        self.send_keys(self.yaml_data["loginPage"]["password"], password)
        self.click(self.yaml_data["loginPage"]["login"])


if __name__ == '__main__':
    login = LoginPage("C")
    login.login(username="system_admin", password="Info2soft")
    time.sleep(10)
