import pandas as pd

# 读取excel数据
df = pd.read_excel('github_data.xlsx')
# 删除包含空值的行
df.dropna(inplace=True)
# 保存修改后的excel
df.to_excel('github_data.xlsx', index=False)