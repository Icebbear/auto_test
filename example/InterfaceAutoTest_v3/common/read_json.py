# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      read_json.py
# Author:       ice bear
# Datetime:     2023/11/3 14:16
# Description:
# 
# ---------------------------------------------------------------------------
import json
import os
from InterfaceAutoTest_v3.common import log


def read_json(filename):
    """读取json文件，将json文件的内容转成python对象，并返回"""
    if os.path.isfile(filename) and filename.endswith(".json"):
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                return json.loads(f.read())
        except:
            log.error("开打json文件获取json文件的内容序列化为python对象失败，请察看json文件是否有错误！！！")
            raise FileExistsError("开打json文件获取json文件的内容序列化为python对象失败，请察看json文件是否有错误！！！")
    else:
        log.error("json文件的路径不合法")
        raise FileNotFoundError("json文件的路径不合法")
