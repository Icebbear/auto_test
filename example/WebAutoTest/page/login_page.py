# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      login_page.py
# Author:       ice bear
# Datetime:     2023/12/2 15:24
# Description:
# 
# ---------------------------------------------------------------------------
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
    login.login("admin", "123456")
    time.sleep(10)

