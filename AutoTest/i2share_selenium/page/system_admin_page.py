# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      system_admin_page.py
# Author:       ice bear
# Datetime:     2023/12/14 10:29
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import time

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from page.login_page import LoginPage


class SystemAdminPage(LoginPage):
    def __init__(self, browser_name):
        super().__init__(browser_name)
        self.login(username="system_admin", password="Info2soft")
        self.click(self.yaml_data["systemAdminPage"]["user_mg"])
        self.click(self.yaml_data["systemAdminPage"]["adduser"])
        time.sleep(2)

    def add_user(self, username, email, pwd1, pwd2, message="1"):
        self.send_keys(self.yaml_data["systemAdminPage"]["username"], username)
        time.sleep(1)
        self.send_keys(self.yaml_data["systemAdminPage"]["email"], email)
        time.sleep(1)
        self.send_keys(self.yaml_data["systemAdminPage"]["pwd1"], pwd1)
        time.sleep(1)
        self.send_keys(self.yaml_data["systemAdminPage"]["pwd2"], pwd2)
        time.sleep(1)
        self.click(self.yaml_data["systemAdminPage"]["confirm"])

        selector_result = self.selector_loader('x,//*[@id="add-user-form"]/div/div/p')
        re = WebDriverWait(self.driver, timeout=20, poll_frequency=1).until(
            EC.presence_of_element_located(selector_result))
        print("-"*20)
        print(re)
        print("-" * 20)
        print(re.text)
        print("-" * 20)
        # if error:
        #     print("添加失败")
        # else:
        #     print("添加成功")
        #     # return "添加成功"
        time.sleep(10)


if __name__ == '__main__':
    s = SystemAdminPage("c")
    s.add_user(username="s005", email="s005@qq.com", pwd1="123qwe-=", pwd2="123qwe-=")
