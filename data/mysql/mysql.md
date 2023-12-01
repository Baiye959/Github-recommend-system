```sql
-- 新建数据库
CREATE DATABASE recommend;

-- 仓库
-- Name	Link	Introduction	Language	Stars	Forks
-- krahets/hello-algo	https://github.com/krahets/hello-algo	《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。	Java	33,255	3,924
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
 ```