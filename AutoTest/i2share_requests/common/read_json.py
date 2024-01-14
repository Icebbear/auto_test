# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   AutoTest
# FileName:      read_json.py
# Author:       ice bear
# Datetime:     2023/12/4 10:51
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import json


def read_json(file_name):
    with open(file_name, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())


if __name__ == '__main__':
    xx = read_json("../config/ice bear/expect_data.json")
    print(xx)
