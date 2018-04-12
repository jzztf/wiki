# mysql常用命令

- 创建数据库

	`create database name;`

- 选择数据库

  `use database name;`

- 删除数据库(不提醒)

	`drop database name;`

- 删除数据库(提醒)

	`mysqladmin drop dabase name;`

- 显示表

	`show tables;`

- 表的详细描述

	`describe tablename;`



--------------------------------------

操作:

# create database
CREATE DATABASE db_name

# use database
USE db_name

# create table
CREATE TABLE table_name(
id INT(11) AUTO_INCRIMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
usename VARCHAR(30),
password VARCHAR(100),
register_date TIMESTAMP DEFULT CURRENT_TIMESTAMP
);

# show table

SHOW tables;
# descript table


# view table

SELECT * FROM table_name


