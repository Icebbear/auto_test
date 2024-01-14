# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      test_dem.py
# Author:       ice bear
# Datetime:     2023/12/2 15:59
# Description:
# 
# ---------------------------------------------------------------------------
import time
import unittest

from parameterized import parameterized

from common.BPM_log import bpm_log
from common.db import DB
from common.read_excel import ReadExcel
from page.dem_page import DemPage


class TestDem(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = DB()
        time_str = time.strftime("%Y_%m_%d_%H_%M_%S")
        cls.loger = bpm_log(time_str+"dem.log")
        cls.dem_page = DemPage("C")

    @parameterized.expand(ReadExcel().get_data())
    def test_add_dem(self, case_data, expect_data, sql_data):
        if sql_data is not None:
            self.db.delete(sql_data)

        result = self.dem_page.add_dem(case_data[0], case_data[1], case_data[2])
        # 断言
        try:
            self.assertEqual(expect_data, result)
        except:
            self.loger.error("断言失败，用例为："+str(case_data)+"。期望结果为:"+str(expect_data))
            raise AssertionError("断言失败")


if __name__ == '__main__':
    unittest.main()
