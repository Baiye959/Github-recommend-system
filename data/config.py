import pymysql

# 建立 MySQL 连接
conn = pymysql.connect(
    host='localhost',
    user='mysql_user_name',
    password='mysql_password',
    db='recommend',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)