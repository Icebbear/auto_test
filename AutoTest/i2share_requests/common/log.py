# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   AutoTest
# FileName:      log.py
# Author:       ice bear
# Datetime:     2023/12/4 10:51
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import logging
import os.path


def write_log():
    logger = logging.getLogger(name="ice bear")
    logger.level = logging.NOTSET

    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report/log/access.log")
    handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    log_format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s - %(name)s')
    handler.setFormatter(log_format)
    logger.addHandler(handler)
    return handler
