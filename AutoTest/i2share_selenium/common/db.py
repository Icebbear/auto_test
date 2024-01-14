# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_selenium
# FileName:      db.py
# Author:       ice bear
# Datetime:     2023/12/13 15:34
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
#
import pymysql

from common.read_ini import ReadIni


class DB:
    def __init__(self):
        ri = ReadIni()
        self.conn = pymysql.connect(
            host=ri.get_sql_message("host"),
            port=int(ri.get_sql_message("port")),
            user=ri.get_sql_message("user"),
            password=ri.get_sql_message("pwd"),
            database=ri.get_sql_message("database"),
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
                raise ValueError("请检查SQL语句是否正确")
        else:
            raise ValueError("请检查SQL语句是否正确")

    def ex(self, sql):
        self.cursor.execute(sql)
        # sql_lower = sql.lower().strip()
        # if sql_lower.startswith("source") and sql_lower.endswith(".sql"):
        #     try:
        #         self.cursor.execute(sql)
        #     except:
        #         raise ValueError("请检查SQL语句是否正确")
        # else:
        #     raise ValueError("请检查SQL语句是否正确")


if __name__ == '__main__':
    db = DB()
    db.ex("source /data/i2share/scripts/i2share_db_init_for_mysql5.sql")