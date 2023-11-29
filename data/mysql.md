```sql
CREATE DATABASE recommend;

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

 CREATE TABLE IF NOT EXISTS `user`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `username` varchar(100) NOT NULL  COMMENT 'username',
    `password` varchar(200) NOT NULL  COMMENT 'password',
    `email` varchar(100) NOT NULL  COMMENT 'wmail',
    PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
 ```