# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      BPM_runner.py
# Author:       ice bear
# Datetime:     2023/12/2 16:09
# Description:
# 
# ---------------------------------------------------------------------------
import unittest
import unittestreport
from common.read_ini import ReadIni

if __name__ == '__main__':
    # 创建suite
    suite = unittest.TestSuite()
    # 创建loader
    loader = unittest.TestLoader()
    # 获取用例层的目录和报告的目录
    read_ini = ReadIni()
    test_case_path = read_ini.get_test_path("test_case")
    report_html_path = read_ini.get_report_path("html")
    # 使用loader将用例加载到测试套中
    suite.addTests(loader.discover(test_case_path, pattern="test*.py"))
    # 创建unittestreport的runner
    runner = unittestreport.TestRunner(
        suite,
        filename="BPM添加维度报告.html",
        report_dir=report_html_path,
        title='BPM添加维度',
        tester='黄总',
        desc="BPM项目测试生成的报告",
        templates=1
    )

    # 启动
    runner.run()