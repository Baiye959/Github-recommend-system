import pandas as pd
import pymysql
from config import conn

# 读取表格信息
filename = 'ratings.csv'
data = pd.read_csv(filename, header=0)

# 建立 MySQL 连接
cursor = conn.cursor()

query = 'insert into ratings(userId,githubId,rating,timestamp) values (%s,%s,%s,%s)'
for i in range(0, len(data)):
#id为自增字段，不需要添加
    userId = data.iloc[i, 0]
    githubId = data.iloc[i, 1]
    rating = data.iloc[i, 2]
    timestamp = data.iloc[i, 3]
    values = (int(userId), int(githubId), float(rating), int(timestamp))
    cursor.execute(query, values)
    
cursor.close()
conn.commit()
print("数据导入成功")
conn.close()
