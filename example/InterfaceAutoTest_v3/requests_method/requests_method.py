# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      requests_method.py
# Author:       xxxxxxx
# Datetime:     2023/11/3 15:24
# Description:
# 
# ---------------------------------------------------------------------------
import base64
import requests
from InterfaceAutoTest_v3.common import log
from InterfaceAutoTest_v3.common.read_ini import ReadIni
from InterfaceAutoTest_v3.data_config.settings import *


class RequestsMethod:
    def __init__(self):
        """关联被测系统的登录状态"""
        login_url = ReadIni().get_host(URL_HOST_CUSTOM) + "/auth"
        login_data = {"username": "admin", "password": base64.b64encode("123456".encode()).decode()}

        self.bpm_session = requests.sessions.Session()
        self.bpm_session.headers.update({"Authorization": "Bearer "+self.bpm_session.post(url=login_url, json=login_data).json().get("token")})

    def request_all(self, req_method, req_url, req_mime=None, case_data=None):
        """封装公共的请求方法"""
        if req_mime == "json" or req_mime == "application/json":
            return self.bpm_session.request(method=req_method, url=req_url, json=case_data)

        elif req_mime == "x-www-form-urlencoded" or req_mime == "application/x-www-form-urlencoded":
            return self.bpm_session.request(method=req_method, url=req_url, data=case_data)

        elif req_mime == "form-data" or req_mime == "multipart/form-data":
            return self.bpm_session.request(method=req_method, url=req_url, files=case_data)

        elif req_mime == "query" or req_mime == "params" or req_mime == "param":
            return self.bpm_session.request(method=req_method, url=req_url, params=case_data)

        elif req_mime is None:
            return self.bpm_session.request(method=req_method, url=req_url)

        # 判断媒体类型是否为query|body 或者 body|query 、json|query、query|json
        elif req_mime == "query|body" or req_mime == "body|query" or req_mime == "json|query" or req_mime == "query|json":
            return self.bpm_session.request(method=req_method, url=req_url, params=case_data["query"], json=case_data["body"])
        else:
            log.error("传入的媒体类型的值错误，请察看excel中是否填入正确")
            raise NameError("传入的媒体类型的值错误，请察看excel中是否填入正确")