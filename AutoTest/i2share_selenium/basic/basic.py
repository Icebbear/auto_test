# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      basic.py
# Author:       zdq
# Datetime:     2023/12/13 19:55
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from common.read_ini import ReadIni


class Basic:
    def __init__(self, browser_name):
        browser_name_lower = browser_name.lower()
        if browser_name_lower == "chrome" or browser_name_lower == "c":
            self.driver = webdriver.Chrome()

        elif browser_name_lower == "edge" or browser_name_lower == "e":
            self.driver = webdriver.Edge()

        elif browser_name_lower == "firefox" or browser_name_lower == "f":
            self.driver = webdriver.Firefox()

        elif browser_name_lower == "ie" or browser_name_lower == "i":
            self.driver = webdriver.Ie()
        else:
            raise NameError("浏览器名称错误")

        self.driver.maximize_window()

        self.read_ini = ReadIni()
        self.driver.get(self.read_ini.get_url("host"))

    def selector_loader(self, strs):
        selector = strs.split(",")[0].strip().lower()  # 定位方式
        loader = strs.split(",")[1].strip()            # 定位的值

        # id
        if selector == "i" or selector == "id":
            return By.ID, loader
        # name
        elif selector == "n" or selector == "name":
            return By.NAME, loader
        # tag name
        elif selector == "t" or selector == "tag_name":
            return By.TAG_NAME, loader
        # class name
        elif selector == "class_name" or selector == "class":
            return By.CLASS_NAME, loader
        # link text
        elif selector == "link_text" or selector == "l":
            return By.LINK_TEXT, loader
        # partial link text
        elif selector == "p" or selector == "partial_link_text":
            return By.PARTIAL_LINK_TEXT, loader
        # xpath
        elif selector == "x" or selector == "xpath":
            return By.XPATH, loader
        # css selector
        elif selector == "c" or selector == "css_selector" or selector == "css":
            return By.CSS_SELECTOR, loader

        else:
            raise NameError("传入定位方式错误")

    def presence(self, strs):
        selector_result = self.selector_loader(strs)
        return WebDriverWait(self.driver, timeout=20, poll_frequency=1).until(EC.presence_of_element_located(selector_result))

    def clickable(self, strs):
        selectors_result = self.selector_loader(strs)
        return WebDriverWait(self.driver, timeout=20, poll_frequency=1).until(EC.element_to_be_clickable(selectors_result))

    def send_keys(self, strs, value):
        element = self.presence(strs)
        element.send_keys(value)

    def click(self, strs):
        element = self.clickable(strs)
        element.click()

    def quit(self):
        self.driver.close()

    def close(self):
        self.driver.close()
