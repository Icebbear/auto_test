# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_requests
# FileName:      test_admin.py
# Author:       zdq
# Datetime:     2023/12/12 16:07
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import pytest
import allure
from common.read_excel import ReadExcel


class TestAdmin:
    @allure.epic("i2share_admin")
    @pytest.mark.parametrize(
        "module_name, api_name, title, level, case_method, case_url, case_mine, case_data, case_expect, sql_type, "
        "sql_data, update_key",
        ReadExcel(table_name="用户管理",
                  excel_name="zdq/APIAutoTest.xlsx",
                  case_data_name="zdq/case_data.json",
                  expect_data_name="zdq/expect_data.json"
                  ).get_data())
    def test_admin(self, req_fix, module_name, api_name, title, level, case_method, case_url, case_mine, case_data,
              case_expect, sql_type, sql_data, update_key):
        allure.dynamic.feature(module_name)
        allure.dynamic.story(api_name)
        allure.dynamic.title(title)
        allure.dynamic.severity(level)
        res = req_fix.request_all(req_method=case_method, req_url=case_url, req_mime=case_mine, case_data=case_data)


        try:
            assert case_expect in res.text
        except:
            raise "断言失败"


if __name__ == '__main__':
    pytest.main()
