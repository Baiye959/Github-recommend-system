import pymysql

# 建立 MySQL 连接
conn = pymysql.connect(
    host='localhost',
    user='debian-sys-maint',
    password='ET8f5F3qMOvqPnbM',
    db='recommend',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
