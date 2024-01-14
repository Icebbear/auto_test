# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      dem.py
# Author:       ice bear
# Datetime:     2023/12/2 15:31
# Description:
# 
# ---------------------------------------------------------------------------
import os
import time

from faker import Faker

from page.login_page import LoginPage


class DemPage(LoginPage):
    def __init__(self, browse_name):
        super().__init__(browse_name)
        self.login("admin", "123456")
        self.click(self.yaml_data["demPage"]["user"])
        self.click(self.yaml_data["demPage"]["org"])
        self.click(self.yaml_data["demPage"]["dem"])

    def add_dem(self, dem_name, dem_code, dem_message=""):
        self.click(self.yaml_data["demPage"]["add_dem"])
        self.send_keys(self.yaml_data["demPage"]["dem_name"], dem_name)

        time.sleep(2)
        if dem_name.strip():
            self.click(self.yaml_data["demPage"]["dem_code"])
            time.sleep(1)
            self.click(self.yaml_data["demPage"]["quit"])

        self.send_keys(self.yaml_data["demPage"]["dem_code"], dem_code)

        self.click(self.yaml_data["demPage"]["save"])

        time.sleep(1)
        text = self.presence(self.yaml_data["demPage"]["message"])
        print(text)
        print(text.text)


        # if "成功" not in text:
        #     self.click(self.yaml_data["demPage"]["dem_quit"])

        # 解图
        # 图片名称
        img_name = str(dem_name) + "==" + str(dem_code) + ".png"
        self.driver.get_screenshot_as_file(os.path.join(self.read_ini.get_report_path("img"), img_name))
        return text


if __name__ == '__main__':
    dem = DemPage("C")
    data = Faker(locale="zh_cn")
    # for i in range(3):
    #     print(dem.add_dem(data.name(), "@#!#!#!#!#"))
    dem.add_dem(data.name(), "d1f")