# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      log.py
# Author:       ice bear
# Datetime:     2023/11/3 14:02
# Description:
# 
# ---------------------------------------------------------------------------
import logging
import os


def write_log():
    """创建写入日志对象"""
    logger = logging.getLogger(name="黄总")
    logger.level = logging.NOTSET
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report/log/日志汇总.log")
    handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s - %(name)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger
