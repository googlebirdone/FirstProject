import pymysql
import requests
from jsonpath import jsonpath


class DB:
    def __init__(self, host, port: int, user, pswd, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=pswd, db=db,
                                    charset='utf-8')

    def handle_db(self, sql, method=None):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if method is None:
            return cursor.fetchall()
        else:
            self.conn.commit()

    def close_db(self):
        self.conn.cursor.close()
        self.conn.close()


class RequestJson:
    def json_parse(self, json_path, expr):
        return jsonpath(json_path, expr)

    def request(self, method, url, **kwargs):
        res = requests.request(method=method, url=url, **kwargs)
        return res.json()


