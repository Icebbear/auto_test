# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      test_dem.py
# Author:       ice bear
# Datetime:     2023/12/16 10:21
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import time
import unittest

from parameterized import parameterized

from common.db import DB
from common.i2share_log import i2share_log
from common.read_excel import ReadExcel
from page.system_admin_page import SystemAdminPage


class TestDem(unittest.TestCase):
    def setUpClass(self) -> None:
        self.db = DB
        time_str = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.loger = i2share_log(time_str + "i2share_se.log")
        self.system_admin_page = SystemAdminPage("c")

    def tearDown(self):
        self.system_admin_page.close()

    @parameterized.expand(ReadExcel().get_data())
    def test_add_user(self, case_data, expect_data, sql_data):
        result = self.system_admin_page.add_user(
            username=case_data[0],
            email=case_data[1],
            pwd1=case_data[2],
            pwd2=case_data[3]
        )
        print(result)
        # try:
        #     self.assertEquals(expect_data, result)
        # except:
        #     self.loger.error("断言失败，用例为：" + str(case_data) + "。期望结果为:" + str(expect_data))
        #     raise AssertionError("断言失败")


if __name__ == '__main__':
    unittest.main()
