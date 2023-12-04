# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      db.py
# Author:       xxxxxxx
# Datetime:     2023/11/3 14:23
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql

from InterfaceAutoTest_v3.common import log
from InterfaceAutoTest_v3.common.read_ini import ReadIni
from InterfaceAutoTest_v3.data_config.settings import *


class DB:
    def __init__(self):
        """链接数据库，获取链接对象和游标对象"""
        read_ini = ReadIni()
        try:
            self.conn = pymysql.connect(
                host=read_ini.get_sql_message(HOST),
                port=int(read_ini.get_sql_message(PORT)),
                user=read_ini.get_sql_message(USER),
                password=read_ini.get_sql_message(PWD),
                database=read_ini.get_sql_message(DATABASE),
                charset="utf8"
            )
            self.cursor = self.conn.cursor()
        except:
            log.error("链接数据库错误或者获取游标对象失败！！！，请求察看数据库的链接配置.")
            raise pymysql.MySQLError("链接数据库错误或者获取游标对象失败！！！，请求察看数据库的链接配置.")

    def close(self):
        self.cursor.close()
        self.conn.close()

    def delete(self, sql):
        """执行删除的sql语句"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            log.error("执行删除的sql语句错误，请察看对应的删除的sql语句")
            raise ValueError("执行删除的sql语句错误，请察看对应的删除的sql语句")

    def select(self, sql, num=1):
        """执行查询的sql语句"""
        try:
            self.cursor.execute(sql)
            select_result = self.cursor.fetchall()
            if select_result and num == 1:
                return select_result[0][0]
            elif select_result and num == 2:
                return select_result[0][0], select_result[0][1]
            elif select_result and num > 3:
                return select_result
        except:
            log.error("执行查询的sql语句错误，请察看对应的查询的sql语句")
            raise ValueError("执行查询的sql语句错误，请察看对应的查询的sql语句")


if __name__ == '__main__':
    db = DB()
    sql = """SELECT * FROM uc_demension LIMIT 1"""
    print(db.select(sql))
