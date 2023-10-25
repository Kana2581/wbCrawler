import mysql.connector
import res
# 连接到MySQL数据库


def save(data):
    cursor = res.db_connection.cursor()

# 构建插入语句
    for i in range(len(data)):
        print(', '.join(list(data[i].values())))
        insert_query = f"INSERT INTO texts ({', '.join(data[i].keys())}) VALUES ({', '.join(['%s' for _ in data[i].values()])})"
       
# 执行插入
        print(insert_query)
        cursor.execute(insert_query,list(data[i].values()))

# 提交更改并关闭连接
