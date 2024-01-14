# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      conftest.py
# Author:       ice bear
# Datetime:     2023/11/3 15:33
# Description:
# 
# ---------------------------------------------------------------------------
import pytest
from InterfaceAutoTest_v3.common.db import DB
from InterfaceAutoTest_v3.requests_method.requests_method import RequestsMethod


@pytest.fixture(scope="session")
def req_fix():
    req = RequestsMethod()
    yield req


@pytest.fixture(scope="session")
def db_fix():
    db = DB()
    yield db
    db.close()


# 黄总定义的自定义固件，请勿乱动=================start=========>

# <====================================================end
#
# def pytest_collection_modifyitems(items):
#     # item表示每个测试用例，解决用例名称中文显示问题
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
