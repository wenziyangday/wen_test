# -*- coding: utf-8 -*-
import pymysql
from common.config import Config


# todo 学习一下pymysql 的相关操作
class Sql:
    # mysql 操作类
    def __init__(self):
        self.db_conf = Config()
        host = self.db_conf.get_named_key('Mysql-Database', 'host')
        db = self.db_conf.get_named_key('Mysql-Database', 'db')
        user = self.db_conf.get_named_key('Mysql-Database', 'user')
        password = self.db_conf.get_named_key('Mysql-Database', 'password')
        charset = self.db_conf.get_named_key('Mysql-Database', 'charset')
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()

    # 执行一条sql 语句 （增、删、改）
    def execute_sql(self, sql, data):
        self.cur.execute(sql, data)
        self.conn.commit()

    # 查询
    def search(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    # 关闭数据库
    def close_mysql(self):
        self.cur.close()
        self.conn.close()
