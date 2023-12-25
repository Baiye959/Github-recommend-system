# 用户手册
Demo：[http://47.106.213.193:5000/](http://47.106.213.193:5000/)

##  项目结构

```Bash
root@xxxxxxx:~/Github-recommend-system-main$ tree
.
├── data # 项目启动前操作
│   ├── data # 数据预处理
│   └── mysql # 建数据表、数据存入数据库
└── html # 项目代码
    ├── app.py # flask在线服务
    ├── blueprints # 后端蓝图
    ├── config.py # 数据库配置1
    ├── exts.py # 数据库配置2
    ├── models.py # 数据表对应class
    ├── scheduled # als定时任务
    │   ├── als_model # als模型
    │   ├── als.py # als算法
    │   ├── app.py # flask在线服务
    │   └── config.py # 数据库配置
    ├── static # 静态文件
    └── template # 前端

```

## 5.2 环境配置

注：本项目在ubuntu20.04云服务器上测试通过

requirements.txt

```text
faker
pandas
scikit-learn
pyspark
flask
pymysql
openpyxl
flask-login
gevent
flask-sqlalchemy
flask-wtf
email-validator
PyEmail
flask_apscheduler
faiss-gpu

```

```Bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python-is-python3 unzip openjdk-8-jdk apache2 mysql-server screen
pip install -r requirements.txt
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /etc/profile
source /etc/profile
```

## 5.3 启动项目

1. 打开防火墙的5000端口(flask在线服务)
2. 修改配置信息

    mysql数据库本地账号密码信息查询

```Bash
sudo cat /etc/mysql/debian.cnf
```

    将项目中的config文件均修改为自己的数据库账号密码
3. 创建数据库、数据表

```SQL
-- 新建数据库
CREATE DATABASE recommend;

-- 仓库
-- Name  Link  Introduction  Language  Stars  Forks
-- krahets/hello-algo  https://github.com/krahets/hello-algo  《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。  Java  33,255  3,924
CREATE TABLE IF NOT EXISTS `github_info`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` varchar(1000) NOT NULL  COMMENT 'name',
    `link` varchar(1000) NOT NULL  COMMENT 'link',
    `introduction` varchar(5000) NOT NULL  COMMENT 'introduction',
    `language` varchar(64) NOT NULL  COMMENT 'language',
    `stars` int NOT NULL  COMMENT 'stars',
    `forks` int NOT NULL  COMMENT 'forks',
    PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 评分
-- userId,githubId,rating,timestamp
-- 1,1,4,964982703
 CREATE TABLE IF NOT EXISTS `ratings`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `userId` int NOT NULL  COMMENT 'userId',
    `githubId` int NOT NULL  COMMENT 'githubId',
    `rating` float NOT NULL  COMMENT 'rating',
    `timestamp` int NOT NULL  COMMENT 'timestamp',
    PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 用户
-- username,password,email
-- Mary Swanson,431f87b87f999f5a502411b25c038a128fe86b7c,twright@example.net
 CREATE TABLE IF NOT EXISTS `user`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `username` varchar(100) NOT NULL  COMMENT 'username',
    `password` varchar(200) NOT NULL  COMMENT 'password',
    `email` varchar(100) NOT NULL  COMMENT 'email',
    PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
 
-- 收藏
-- userId,githubId
-- 1,1
 CREATE TABLE IF NOT EXISTS `collect`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `userId` int NOT NULL  COMMENT 'userId',
    `githubId` int NOT NULL  COMMENT 'githubId',
    PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```
4. 用户数据生成

```Bash
cd data/data
python test_user.py
```
5. 录入数据

```Bash
cd data/mysql
python xlsx2mysql.py csv2mysql.py csv2mysql_rating.py

```
6. 运行一次ALS算法

```Bash
cd html/scheduled
python als.py
```
7. 启动flask服务

```Bash
cd html
python app.py
cd html/scheduled
python app.py
```

此时浏览器访问公网ip:5000即可看到在线网站服务
