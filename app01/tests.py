import pymysql
from django.test import TestCase

# Create your tests here.


def connect_db(host, db_user, pwd, db_name):
    db = pymysql.connect(host=f"{host}", user=f"{db_user}", password=f"{pwd}", db=f"{db_name}", port=3306,
                             charset='utf8')
    return db


db = connect_db("118.195.188.25", "root", "123456789", "hwc")