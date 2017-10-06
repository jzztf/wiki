# 部署jekyll到github

## Jekyll的本地安装

[Jekyll中文文档](http://jekyll.com.cn/)

## 环境需求

- Linux, Unix, or Mac OS X
- Ruby
- RubyGems

## 安装jekyll

借助 RubyGems　安装jekyll

```bash
$ gem install jekyll
```

## 更新jekyll(如果有老版本,需root)

```bash
$ gem update jekyll
```

## 快速开始

```bash
$ gem install jekyll bundler
$ jekyll new myblog
$ cd myblog
/myblog $ jekyll serve
# 根据提示打开浏览器访问"http://127.0.0.1:40000"
```

## 发布文章

_posts 目录为发布文章的目录，编辑markdown文件，存到这里，编译开启http服务即可预览效果

```bash
$ jekyll build	
# 当前文件夹中的内容将会生成到 ./_site 文件夹中
$ jekyll serve build --watch	
# 开启http服务，编译文件夹中内容到./_site，随时监测文件夹中变化，实时预览
$ jekyll serve build --dewatch（或-B）	
# 功能同上，后台运行，终端不显示修改了哪些文件，需关闭时，ps -aux查看后台进程
```

文件名须符合格式: 

`YYYY-MM-DD-name-of-post.ext`

文章头信息：

```
---
layout: post
title:  "title of the article"
date:   YYYY-MM-DD 
---


## 将本地安装部署到github

在github创建`project-name.github.io`库

> 必须创建一个符合`XXX.github.io`格式的库，作为访问网址。github默认此命名的库为页面。

将在github网站上创建的库，clone到本地

```bash
$ git clone <版本库的网址> <本地目录名>
```

将本地搭建好的jekyll和网上clone下来的库合并

> 将之前本地化的jekyll目录下的文件都复制到clone下来的库里，库中之前的文件都删除，只剩README。

进入命令行，实施一次提交(git的基本操作)

```bash
$ add .
$ git commit -m "add jekyll"
$ git push origin master
```

查看页面

> 打开"http://project-name.github.io"就可以查看自己的页面了

## 快速克隆其他博客

在本地jekyll环境都搭建好后，从`https://github.com/jekyll/jekyll/wiki/Sites`　fork一个博客，clone到本地，修改其`_config.yml`，可以直接使用

## 其他一些配置

创建忽略文档

```
.gitiginore
# 忽略“_site”下的文件
_site/*
```

---

<div align="right">**[↑ TOP](#Jekyll的本地安装)**</div>
