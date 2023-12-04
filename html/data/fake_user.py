from faker import Faker
import pandas as pd
import hashlib

fake = Faker(locale='zh_CN')
csv_file = 'user.csv'
df = pd.read_csv(csv_file)
sha1 = hashlib.sha1()

for rowId in range(1, 611):
    data = fake.password()
    sha1.update(data.encode('utf-8'))
    sha1_data = sha1.hexdigest()
    df.loc[rowId]=[fake.name(),sha1_data,fake.email()]

df.to_csv('user.csv',index=False,encoding="utf-8")