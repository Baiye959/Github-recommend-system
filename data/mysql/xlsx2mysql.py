import pandas as pd
import pymysql
from config import conn

# 读取表格信息
filename = 'github_data.xlsx'
data = pd.read_excel(filename, header=1)

# 建立 MySQL 连接
cursor = conn.cursor()

query = 'insert into github_info(name,link,introduction,language,stars,forks) values (%s,%s,%s,%s,%s,%s)'
for i in range(0, len(data)):
#id为自增字段，不需要添加
    name = data.iloc[i, 0]
    link = data.iloc[i, 1]
    introduction = data.iloc[i, 2]
    language = data.iloc[i, 3]
    stars = data.iloc[i, 4]
    forks = data.iloc[i, 5]
    values = (str(name), str(link), str(introduction), str(language), int(stars), int(forks))
    cursor.execute(query, values)
    
cursor.close()
conn.commit()
print("数据导入成功")
conn.close()
