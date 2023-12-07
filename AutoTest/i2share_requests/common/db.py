# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   AutoTest
# FileName:      db.py
# Author:       zdq
# Datetime:     2023/12/4 10:51
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import pymysql

from common.read_ini import ReadIni


class DB:
    def __init__(self):
        read_ini = ReadIni()
        self.conn = pymysql.connect(
            host=read_ini.get_sql("host"),
            port=int(read_ini.get_sql("port")),
            user=read_ini.get_sql("user"),
            password=read_ini.get_sql("pwd"),
            database=read_ini.get_sql("database"),
            charset="utf8"
        )

        self.cursor = self.conn.cursor()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def select(self, sql):
        self.cursor.execute(sql)
        select_result = self.cursor.fetchall()
        return select_result

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    xx = db.select("select * from Admin;")
    print(type(xx))
