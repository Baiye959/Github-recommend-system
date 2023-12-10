from faker import Faker
import pandas as pd
from werkzeug.security import generate_password_hash

fake = Faker(locale='en-US')
csv_file1 = 'user.csv'
csv_file2 = 'password.csv'
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)

for rowId in range(1, 611):
    real_password = fake.password()
    name = fake.name()
    email = fake.email()
    password = generate_password_hash(real_password)
    df1.loc[rowId]=[name,password,email]
    df2.loc[rowId]=[name,password,email,real_password]

df1.to_csv('user.csv',index=False,encoding="utf-8")
df2.to_csv('password.csv',index=False,encoding="utf-8")