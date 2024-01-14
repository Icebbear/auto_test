# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      read_json.py
# Author:       ice bear
# Datetime:     2023/12/13 15:34
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import json


def read_json(filepath):
    with open(filepath, mode="r", encoding="utf-8") as fp:
        return json.load(fp)


if __name__ == '__main__':
    xx = read_json(r"D:\1备份\auto_test\AutoTest\i2share_selenium\data_config\case_data.json")
    print(xx)
