# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_requests
# FileName:      requests_method.py
# Author:       ice bear
# Datetime:     2023/12/6 17:25
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import requests
import re
from common.read_ini import ReadIni
from config.settings import *


class RequestsMethod:
    def __init__(self):
        """
        获取管理员的登录session，并更新值headers中
        """
        host = "http://114.67.239.168"
        login_url = "http://114.67.239.168/ajax/tfa_login/verify/"
        login_data = "username=system_admin&password=YxEz%2BU0hfRocO1%2FuQuNgeKocqqupJAMYwgg0iZws7L3rPpGmW4YoOjIiMjF6DM%2Bu"
        self.i2share_session = requests.sessions.Session()
        result = self.i2share_session.get(url=host)
        x_csrftoken = re.findall(r"value=\'(.+)\'", result.text)
        cookie = result.headers.get("Set-Cookie")
        csrftoken = re.findall(r"csrftoken=\w+", cookie)
        sessionid = re.findall(r"sessionid=\w+", cookie)
        co = csrftoken[0] + "; " + sessionid[0] + ";"
        self.i2share_session.headers.update({"X-CSRFToken": x_csrftoken[0],
                                        "cookie": co,
                                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
        login_result = self.i2share_session.post(url=login_url, data=login_data)

        adminlogin_url = "http://114.67.239.168/accounts/adminlogin/"
        adminlogin_data = "csrfmiddlewaretoken=" + x_csrftoken[
            0] + "&" + "adminpassword=BqNkb2IONZxZPvUcl%2FUTnv1qiVBzmvUX%2FSz59imAv2f8ZZ3ZYGUq538jFZMNo8U%2F&adminname=system_admin"
        if "ok" in login_result.text:
            # self.i2share_session.headers.pop("X-CSRFToken")
            self.i2share_session.headers.update({"Upgrade-Insecure-Requests": "1", "X-Requested-With": "XMLHttpRequest"})
            adminlogin_result = self.i2share_session.post(url=adminlogin_url, data=adminlogin_data, allow_redirects=False)
            new_sessionid = re.findall(r"sessionid=\w+", adminlogin_result.headers.get("Set-Cookie"))
            new_cookie = csrftoken[0] + "; " + new_sessionid[0] + ";"
            self.i2share_session.headers.update({"Cookie": new_cookie})

    def request_all(self, req_method, req_url, req_mime=None, case_data=None):
        if req_mime == "x-www-form-urlencoded" or req_mime == "application/x-www-form-urlencoded":
            return self.i2share_session.request(method=req_method, url=req_url, data=case_data)
        elif req_mime == "json" or req_mime == "application/json":
            return self.i2share_session.request(method=req_method, url=req_url, json=case_data)
        elif req_mime == "form-data" or req_mime == "multipart/form-data":
            return self.i2share_session.request(method=req_method, url=req_url, files=case_data)
        elif req_mime == "query" or req_mime == "params" or req_mime == "param":
            return self.i2share_session.request(method=req_method, url=req_url, params=case_data)
        elif req_mime is None:
            return self.i2share_session.request(method=req_method, url=req_url)
        elif req_mime == "query|body" or req_mime == "body|query" or req_mime =="json|query" or req_mime == "query|json":
            return self.i2share_session.request(method=req_method, url=req_url, params=case_data["query"], json=case_data["body"])


if __name__ == '__main__':
    i2 = RequestsMethod()
    dep_url = "http://114.67.239.168/ajax/tfa_login/verify/"
    data = "username=system_admin&password=YxEz%2BU0hfRocO1%2FuQuNgeKocqqupJAMYwgg0iZws7L3rPpGmW4YoOjIiMjF6DM%2Bu"
    re = i2.request_all(req_url=dep_url, req_method="post", req_mime="x-www-form-urlencoded",case_data=data)
    print(re.text)


