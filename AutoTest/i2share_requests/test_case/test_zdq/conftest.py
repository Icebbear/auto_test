# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_requests
# FileName:      conftest.py
# Author:       ice bear
# Datetime:     2023/12/12 17:02
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import pytest

from requests_method.requests_method import RequestsMethod


@pytest.fixture(scope="session")
def req_fix():
    req = RequestsMethod()
    yield req
