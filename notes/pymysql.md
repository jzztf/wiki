# pythonmysq的安装和使用

## 查看pip-list

`$ pip list`



## 安装mysql



- 查看版本
  - `mysqladmin --version`
- mysql默认密码为空,直接
  - `mysql`可以登录
  - `mysqladmin -u root password "password"创建用户密码 `
- 连接到mysql服务器
  - `mysql -u root -p`会让输入密码
    - `-u`是user
    - `-p`是password

## mysql 管理

- 查看mysql服务
  - 方法一
  ```
  $ ps -ef | grep mysql
  ```
  - 方法二
  ```
  $ netstat -nlp
  ```
- 启动
  - 方法一
  ```
  $ cd /usr/bin
  $ ./mysqld_safe &
  ```
  - 方法二
  ```
  $ service mysql start
  $ service mysql restart # 重启
  ```
- 关闭
  - 方法一
  ```
  $ mysqladmin -u root shutdown
  ```
  - 方法二
  ```
  $ service mysql stop
  ```

    - `cd /usr/bin`
    - `./mysqld_safe &`
  - 关闭
    - `cd /usr/bin`
    - `./mysqladmin -u root -p shutdown`

## 使用mysql

- 查看databases
  - `show databases;`
- 创建新数据库
  - `create database temp;`