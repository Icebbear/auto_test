# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      read_json.py
# Author:       xxxxxxx
# Datetime:     2023/12/2 11:41
# Description:
# 
# ---------------------------------------------------------------------------
import json


def read_json(filepath):
    with open(filepath, mode="r", encoding="utf-8") as fp:
        return json.load(fp)
