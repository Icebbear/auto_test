# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      read_yaml.py
# Author:       ice bear
# Datetime:     2023/12/2 11:42
# Description:
# 
# ---------------------------------------------------------------------------
import yaml


def read_yaml(filepath):
    with open(filepath, mode="r", encoding="utf-8") as fp:
        return yaml.load(fp, Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(read_yaml(r"D:\课程\unittest_learning\WebAutoTest\data_config\data.yaml"))