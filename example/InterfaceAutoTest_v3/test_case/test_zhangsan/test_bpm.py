# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      test_bpm.py
# Author:       ice bear
# Datetime:     2023/11/3 15:33
# Description:
# 
# ---------------------------------------------------------------------------
import pytest
from InterfaceAutoTest_v3.common import log
from InterfaceAutoTest_v3.common.read_excel import ReadExcel
import allure


class TestBPM:

    @allure.epic("BPM项目-老黄")
    # @allure.feature("模块名称")
    # @allure.story("接口名称")
    # @allure.title("用例标题")
    # @allure.severity("用例等级")
    @pytest.mark.parametrize("module_name, api_name, title, level, case_url, case_method, case_mime, case_data, "
                             "expect_data, sql_type, sql_data, update_key", ReadExcel("BPM", "zhangsan/APIAutoTest.xlsx", "zhangsan/case_data.json", "zhangsan/expect_data.json", "zhangsan/sql_data.json").get_data())
    def test_bpm(self, db_fix, req_fix, module_name, api_name, title, level, case_url, case_method, case_mime,
                 case_data, expect_data, sql_type, sql_data, update_key):
        # 影响allure报告的数据，不影响代码流程
        allure.dynamic.feature(module_name)
        allure.dynamic.story(api_name)
        allure.dynamic.title(title)
        allure.dynamic.severity(level)

        # 判断sql语句的类型是否为delete
        if sql_type == "delete":
            # 使用DB类对象执行删除的sql语句
            db_fix.delete(sql_data)
            # 使用RequestsMethod类对象发送请求--pass
        # 判断sql语句类型是否为select
        elif sql_type == "select":
            # 使用DB类对象执行查询的sql语句，并接收查询的结果
            select_result = db_fix.select(sql_data)
            # 将查询结果更新到用例数据中
            case_data[update_key] = select_result
            # 使用RequestsMethod类对象发送请求--pass

        # 判断sql语句的类型是否为select|delete或者为delete|select
        elif sql_type == "select|delete" or sql_type == "delete|select":
            # 使用DB类对象执行删除的sql语句
            db_fix.delete(sql_data.get("delete"))
            # 使用DB类对象执行查询的sql语句，并接收查询的结果
            select_result = db_fix.select(sql_data.get("select"))
            # 将查询结果更新到用例数据中
            case_data[update_key] = select_result

        # 使用RequestsMethod类对象发送请求
        res = req_fix.request_all(req_method=case_method, req_url=case_url, req_mime=case_mime, case_data=case_data)

        # 断言
        try:
            for key in expect_data:
                assert expect_data[key] == res.json().get(key)
        except:
            log.error("断言失败"+"，用例数据为："+str(case_data)+",期望数据为："+str(expect_data)+",服务器返回的数据为："+res.text)
            raise AssertionError("断言失败")


if __name__ == '__main__':
    pytest.main()