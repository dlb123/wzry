import sys
sys.path.append('../')
import pymysql


def connect_db():
    """
    连接mysql数据库
    :return: 数据库连接以及游标
    """

    conn = pymysql.connect(host="127.0.0.1",
                           user='root',
                           password="qwe123",
                           db='spider',
                           charset="utf8mb4")

    return conn
