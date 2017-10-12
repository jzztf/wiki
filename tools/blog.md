# 搭建个人静态博客

## Jekyll

> jekyll的优点在于，github和coding都是默认支持jekyll的。只需在本地搭建好jekyll，上传master分支，就可以在相应的页面访问了，用起来十分简洁。

- [Jekyll](http://jekyll.com.cn/)
- [my notes](#!tools/blog/jekyll.md)

##  Hexo

> hexo优于jekyll的一个好处是可以在命令行直接生成文章，而且文章中不需要再手动添加日期，标签等。更换主题方便，而且next主题真好用，有标签云，存档，还有主题用起来很简单。麻烦一点的是如果要为博客备份需要创建分支，平时在备份分支编辑操作，然后发布master分支。

- [Hexo](https://hexo.io/)
- [my notes](#!tools/blog/hexo.md)

## MDwiki

> mdwiki的优点在于随时可以将markdown文件放入相应文件夹，在目录文件或导航文件添加链接即可访问，用于个人博客或文章整理很是方便

- [MDwiki](http://dynalon.github.io/mdwiki/#!index.md)
- [my notes](#!tools/blog/mdwiki.md)

## Gollum wiki

> gollumwiki的优点在于每次更新都可以看到修改记录，自动记录页面的生成情况。个人感觉在浏览器中编辑不舒服。不过用来做项目，需要一点点修改的文档，那是再好不过。

- [Gollumwiki](https://github.com/gollum/gollum)
- [my notes](#!tools/blog/gollumwiki.md)

## 在github&coding 部署静态网站

- jekyll和mdwiki 只需将”master“分支上传即可

- hexo 如果需要备份，则需要创建新分支比如“gh-pages”或者“coding-pages”,备份仓库，而”master“分支用来发布

## github域名绑定(github)

进入域名管理

- 添加A记录

```
A|@|192.30.252.153
A|@|192.30.252.154
```

- 添加CNAME

```
CNAME|@|jzztf.github.io
```

## 将一个仓库同时上传到两个仓库(github&coding)

两个仓库只需创建，不需要初始化(不自动生成README)；设置不同的远程仓库；分别推送

```bash
$ git remote add origin_repo_1 git@github...  # 添加github远程仓库
$ git remote add origin_repo_2 git@coding...  # 添加coding远程仓库
$ git pull origin_repo_1 master # 因为没有初始化远程仓库，此项操作不会有内容
$ git pull origin_repo_2 master
$ git push origin_repo_1 master  # 分别推送到远程仓库
$ git push origin_repo_2 master
```

---
<div align="right">**[↑ TOP](#Jekyll)**</div>