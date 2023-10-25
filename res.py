import mysql.connector
header={'Cookies':'***',
            'User-Agent':'***'}


# 连接到MySQL数据库
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="wb"
)