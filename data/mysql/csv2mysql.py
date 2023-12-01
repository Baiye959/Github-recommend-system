import pandas as pd
import pymysql
from config import conn

# 读取表格信息
filename = 'user.csv'
data = pd.read_excel(filename, header=1)

# 建立 MySQL 连接
cursor = conn.cursor()

query = 'insert into user(username,password,email) values (%s,%s,%s)'
for i in range(0, len(data)):
#id为自增字段，不需要添加
    username = data.iloc[i, 0]
    link = data.iloc[i, 1]
    introduction = data.iloc[i, 2]
    values = (str(username), str(password), str(email))
    cursor.execute(query, values)
    
cursor.close()
db.commit()
print("数据导入成功")
db.close()
