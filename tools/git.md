# git常用命令

## git install

```bash
$ sudo apt-get install git
```

## git config

- `git config --global user.name "uesername"`
- `git config --global user.email "useremail"`
- `git config --list`

## git基本使用

```bash
cd repo/
# 初始化"git"仓库
git init
touch readme.md
# 将"readme.md"添加到"git"仓库暂存区
git add readme.md
# 将"readme.md"提交到仓库
git commit -m "add readme.md"
echo “Hello world!” > readme.md
# 将修改后文件添加到仓库暂存区？
git add readme.md
# 将修改后文件提交到仓库
git commit -m "update readme.md"
```
## ssh key

```bash
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

##  github远程仓库

```bash
$ git remote add origin git@git...
$ git remote list
$ git remote remove origin
$ git pull origin master
$ git push origin master
$ git push origin branch
```

## git 分支

```bash
$ git checkout -b new_branch
等同于
$ git branch new_branch
$ git checkout new_branch
```
## 将本地仓库同步到两个远程仓库

- 创建本地仓库(自带README.md)
- 创建两个远程仓库(不用创建“README.md”初始化)
- 在本地添加两个远程仓库
  - `git remote add coding git@...`
  - `git remote add github git@...`
- 分别“pull“和”push“
  - `git pull coding master`
  - `git push coding master`








---

<div align="right">**[↑ TOP](#git install)**</div>
