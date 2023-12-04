# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57_unittest
# FileName:      db.py
# Author:       xxxxxxx
# Datetime:     2023/12/2 14:23
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql

from common.read_ini import ReadIni


class DB:
    def __init__(self) -> object:
        read_ini = ReadIni()
        self.conn = pymysql.connect(
            host=read_ini.get_sql_message("host"),
            port=int(read_ini.get_sql_message("port")),
            user=read_ini.get_sql_message("user"),
            password=read_ini.get_sql_message("pwd"),
            database=read_ini.get_sql_message("database"),
            charset="utf8"
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def delete(self, sql):
        sql_lower = sql.lower().strip()
        if sql_lower.startswith("delete") and sql_lower.endswith(";"):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except:
                raise ValueError("请查看sql语句是否正常")
        else:
            raise ValueError("请查看sql语句是否正常")


if __name__ == '__main__':
    db = DB()
