# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      i2Share_runner.py
# Author:       ice bear
# Datetime:     2023/12/16 10:12
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import unittest

import unittestreport

from common.read_ini import ReadIni

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    read_ini = ReadIni()
    test_case_path = read_ini.get_test_path("test_case")
    report_html_path = read_ini.get_report_path("html")

    suite.addTests(loader.discover(test_case_path, pattern="test*.py"))

    runner = unittestreport.TestRunner(
        suite,
        filename="i2share添加用户测试报告",
        report_dir=report_html_path,
        title="添加用户",
        tester="bear",
        desc="i2Share添加用户测试生成的报告",
        templates=1
    )

    runner.run()
