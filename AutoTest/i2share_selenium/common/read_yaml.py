# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      read_yaml.py
# Author:       zdq
# Datetime:     2023/12/13 15:34
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import yaml


def read_yaml(filepath):
    with open(filepath, mode="r", encoding="utf-8") as fp:
        return yaml.load(fp, Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(read_yaml(r"D:\1备份\auto_test\AutoTest\i2share_selenium\data_config\data.yaml"))