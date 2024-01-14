# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_requests
# FileName:      requests_method.py
# Author:       icebear
# Datetime:     2023/12/6 17:25
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import requests
import re
from common.read_ini import ReadIni
from config.settings import *


# class RequestsMethod:
#     def __init__(self):
#         login_url = ReadIni().get_host(SERVER_HOST) + "/"
#
#     def request_all(self):
#         pass


# def login():
#     host = "http://114.67.239.168/accounts/login/?next=/"
#     login_url = "http://114.67.239.168/ajax/tfa_login/verify/"
#     login_data = "csrfmiddlewaretoken=mKndg8Wo16DpenoxIab7XYgwEhaq7movphk0cH6yXwSgdkTWPctwsMa5jw9mQ7d8&adminpassword=nj%2FfRT5Kpa1QQs0UuYnGLpfvwXJNl3Hp6sPnzil6wW1sPbMogwTuQp8er97WgfXr&adminname=system_admin"
#     #bpm_session = requests.sessions.Session()
#
#     # bpm_session.headers.update(
#     #     {"Authorization": "Bearer " + bpm_session.post(url=login_url, json=login_data).json().get("token")})
#
#     # re = i2share_session.request(url=host, method="get")
#     # i2share_csrftoken = requests.request(url=host, method="get").text
#     # print(i2share_csrftoken)
#
#     i2share_session = requests.sessions.Session()
#     result = i2share_session.get(url=host).text
#     token = re.findall(r"value=\'(.+)\'", result)
#
#     print(token[0])
#
# login()