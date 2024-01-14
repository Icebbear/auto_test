# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      i2share_log.py
# Author:       zdq
# Datetime:     2023/12/13 15:35
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import logging
import os
import time

from common.read_ini import ReadIni


def i2share_log(filename):
    logger = logging.getLogger()

    log_path = os.path.join(ReadIni().get_report_path("log"), filename)

    handler = logging.FileHandler(filename=log_path, mode="a", encoding="utf-8")
    format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s - %(name)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    time_str = time.strftime("%Y_%m_%d-%H_%M_%S")
    print(time_str)
    loger = i2share_log(time_str + ".log")
    loger.error("断言失败")
