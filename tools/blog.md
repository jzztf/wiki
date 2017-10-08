# 搭建个人静态博客

## Jekyll

- [Jekyll](http://jekyll.com.cn/)
- [my notes](#!tools/blog/jekyll.md)

##  Hexo

- [Hexo](https://hexo.io/)
- [my notes](#!tools/blog/hexo.md)

## MDwiki

- [MDwiki](http://dynalon.github.io/mdwiki/#!index.md)
- [my notes](#!tools/blog/mdwiki.md)

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
