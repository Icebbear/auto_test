# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      basic.py
# Author:       xxxxxxx
# Datetime:     2023/12/2 14:30
# Description:
# 
# ---------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from common.read_ini import ReadIni


class Basic:
    def __init__(self, browse_name):
        if browse_name == "Chrome" or browse_name == "chrome" or browse_name == "c" or browse_name == "C":
            self.driver = webdriver.Chrome()

        elif browse_name == "Edge" or browse_name == "edge" or browse_name == "e" or browse_name == "E":
            self.driver = webdriver.Edge()

        elif browse_name == "firefox" or browse_name == "Firefox" or browse_name == "f" or browse_name == "F":
            self.driver = webdriver.Firefox()
        else:
            raise NameError("浏览器的名称传入错误")

        self.driver.maximize_window()

        self.read_ini = ReadIni()
        self.driver.get(self.read_ini.get_url("host"))

    def selector_loader(self, strs):
        selector = strs.split(",")[0].strip().lower()   # 定位方式
        loader = strs.split(",")[1].strip()     # 定位的值

        # id
        if selector == "i" or selector == "id":
            return By.ID, loader
        # name
        elif selector == "n" or selector == "name":
            return By.NAME, loader
        # tag_name
        elif selector == "t" or selector == "tag_name" or selector == "tag":
            return By.TAG_NAME, loader
        # class_name
        elif selector == "class_name" or selector == "class" or selector == "class":
            return By.CLASS_NAME, loader
        # link_text
        elif selector == "link_text" or selector == "l" or selector == "link":
            return By.LINK_TEXT, loader
        # partial_link_text
        elif selector == "p" or selector == "partial_link_text" or selector == "partial":
            return By.PARTIAL_LINK_TEXT, loader
        # xpath
        elif selector == "x" or selector == "xpath":
            return By.XPATH, loader
        # css_selector
        elif selector == "c" or selector == "css_selector" or selector == "css":
            return By.CSS_SELECTOR, loader

        else:
            raise NameError("传入的定位方式错误")

    # presence_of_element_located
    def presence(self, strs):
        selector_result = self.selector_loader(strs)
        return WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(selector_result))

    # element_to_be_clickable
    def clickable(self, strs):
        selector_result = self.selector_loader(strs)
        return WebDriverWait(self.driver, 20, 1).until(EC.element_to_be_clickable(selector_result))

    # send_keys
    def send_keys(self, strs, value):
        element = self.presence(strs)
        element.send_keys(value)

    # click
    def click(self, strs):
        element = self.clickable(strs)
        element.click()

    # close
    def close(self):
        self.driver.quit()

