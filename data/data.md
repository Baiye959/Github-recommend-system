# 数据说明
## github_data.xlsx
来源：https://ossinsight.io/
爬取github仓库的名称、链接、简介、语言、Stars、Forks
去除无简介仓库后共40种语言、3737个仓库
数据表：github_data.xlsx
## ratings.csv
来源：https://hellogithub.com/
爬取用户对仓库的评分、时间，用户去敏感化
数据表：ratings.csv
## user.csv
来源：用Faker库生成
执行的python源代码为fake_user.py
数据表：user
## password.csv
来源：用Faker库生成
执行的python源代码为fake_user.py
数据表：无，用于调试时测试登录