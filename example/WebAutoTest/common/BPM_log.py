# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      BPM_log.py
# Author:       xxxxxxx
# Datetime:     2023/12/2 11:32
# Description:
# 
# ---------------------------------------------------------------------------
import logging
import os
import time

from common.read_ini import ReadIni


def bpm_log(filename):
    logger = logging.getLogger()

    # 拼接日志文件的路径
    log_path = os.path.join(ReadIni().get_report_path("log"), filename)

    handler = logging.FileHandler(filename=log_path, mode="a", encoding="utf-8")
    format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s - %(name)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    time_str = time.strftime("%Y_%m_%d-%H_%M_%S")
    print(time_str)
    loger = bpm_log(time_str+".log")
    loger.error("断言失败")