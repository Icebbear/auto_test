# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      system_admin_page.py
# Author:       zdq
# Datetime:     2023/12/14 10:29
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
from page.login_page import LoginPage


class SystemAdminPage(LoginPage):
    def __init__(self, browser_name):
        super().__init__(browser_name)
        self.login(username="system_admin", password="Info2soft")
        self.click(self.yaml_data["systemAdminPage"]["user_mg"])
        # self.click(self.yaml_data["systemAdminPage"]["adduser"])
        # self.send_keys(self.yaml_data["systemAdminPage"]["username"])
        # self.send_keys(self.yaml_data["systemAdminPage"]["email"])
        # self.send_keys(self.yaml_data["systemAdminPage"]["pwd1"])
        # self.send_keys(self.yaml_data["systemAdminPage"]["pwd2"])
        # self.click(self.yaml_data["systemAdminPage"]["confirm"])

    def add_user(self,username, email, pwd1, pwd2, message):


