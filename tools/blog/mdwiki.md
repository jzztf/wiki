# MDwiki 文档

> "MDwiki"用一个"html"文件解析同目录下的“markdown”文件，生成静态网页。

## 搭建本地“MDwiki”

- [MDwiki](http://dynalon.github.io/mdwiki/#!index.md)

- [MDwiki-Download](https://github.com/Dynalon/mdwiki/releases)

下载“MDwiki”文件，目前是“mdwiki-0.6.2.zip”

```bash
$ unzip mdwiki-0.6.2.zip          
$ mv mdwiki-0.6.2 mdwiki
$ tree mdwiki 
mdwiki
├── GPLv3.txt
├── LICENSE.txt
├── mdwiki-debug.html
├── mdwiki.html
├── mdwiki-slim.html
└── README.md
$ cd mdwiki
$ mv mdwiki.html index.html
$ echo '# Hello world' > index.md
```

需要的的唯一文件只是“mdwiki.html”,其他都可以删掉。将"mdwiki.html"更名为“index.html”，在访问时只需要加上"#!index.md"，比如“http://localhost:8080/#!index.md”。

## 搭建本地服务器

```bash
# 安装nvm
$ curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | sh`
# 修改nvm镜像，安装node稳定版本
$ NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node nvm install stable
# 使用“--registry选项”从淘宝镜像下载“http-server”
$ npm --registry=https://registry.npm.taobao.org install -g http-server
```

安装好“http-server”就可以在“mdwiki”目录下使用`http-server`命令启动本地服务器，在“http://localhost:8080/#!index.md”访问自己"mdwiki"。

## 部署设置(Github)

### 部署到`username.github.io/mdwiki` 

- 初始化本地仓库

```bash
$ cd mdwiki
$ git init
```

- 创建分支并初始化提交

```bash
$ git checkout -b gh-pages
$ git add .
$ git commit -m "initial"
```

- 在“github”初始化一个仓库“mdwiki”

- 添加远程地址

```bash
$ git remote add origin git@github.com:[username]/mdwiki.git
$ git push -u origin gh-pages
```

- 在github上“setting”中查看"pages"设置发布"gh-pages"

- 设置成功，"mdwiki"就会发布在`username.github.io/mdwiki`

### 部署到`username.github.io`

此时不需要设置分支，直接拉取“master”分支，提交本地仓库

```bash
$ git pull origin master
$ git push origin master
```

### 部署到“coding”

“github”同“coding”部署方法相同

1. 创建本地仓库
2. 创建远程仓库
3. 本地添加远程仓库链接
4. 拉取远程仓库
5. 推送到远程仓库
6. 查看pages设置


## MarkDown语法

- [markdown-syntax](https://markdown-syntax.com/)

## 添加导航栏

创建`navigation.md`文件，放置于同`mdwiki.html`一个目录下，如下制作菜单：

```markdown
# Your wiki name

[Home](home.md)
[About](about.md)
[Download](download.md)
```

对于更复杂的菜单——有多个项目的可收缩子菜单，如下使用列表和水平线分隔显示：

```markdown
# Your wiki name

[菜单-1]()

  * # 子菜单-1
  * [子菜单 项目1-1](项目1-1.md)
  * [子菜单 项目1-2](项目1-2.md)
  ----
  * # 子菜单-2
  * [子菜单 项目2-1](项目2-1.md)
  * [子菜单 项目2-2](项目2-2.md)
  ----
  * # 子菜单-3
  * [子菜单 项目3-1](项目3-1.md)
  * [子菜单 项目3-2](项目3-2.md)

[菜单-2](菜单-2.md)
[菜单-3](菜单-3.md)

```

注意：

- 如果希望点击“菜单-1”展开列表，则“菜单-1”后面括号需要留空
- 子菜单标题前使用“#”，子菜单之间使用“----”水平线隔开
- 一级菜单之间，如果有子菜单，需要和其他一级菜单之间留空行

## 创建连接

- 链接到外部网站

```markdown
[Google](http:www.google.com)
```

- 链接到内部文件

```markdown
[下载](download.md)
```

## 图片

```markdown
![图片](图片放置位置或链接)
```

注意：如果想以图片组的形势呈现图片，可以用空行进行分组

```markdown
！[图片](路径或链接)

！[图片](路径或链接)
！[图片](路径或链接)

！[图片](路径或链接)
！[图片](路径或链接)
！[图片](路径或链接)
```

上面代码，呈现的是一个单独图片，两个一组的图片，三个一组的图片

### 图片链接

```markdown
[![图片](图片放置位置路径或链接)](图片链接到的地址)
```

注意： 图片链接，就连接的语法将图片的语法标记都包裹起来

## 语法高亮

支持的语法：

Language|keyword
:-|:-
Bash|bash
C#|csharp
Clojure|clojure
C++|cpp
CSS|css
CoffeeScript|coffeescript
CMake|cmake
HTML|html
HTTP|http
Java|java
JavaScript|javascript
JSON|json
Markdown|markdown
Objective C|objectivec
Perl|perl
PHP|php
Python|python
Ruby|ruby
R|r
SQL|sql
Scala|scala
Vala|vala
XML|xml

## 主题设置

- 修改“navigation.md”
    - `gimmick:themechooser` 是一个主题选择器。可以不填，也可以添加`<!-- -->`注释掉。
    - `gimmick:theme` 则选择指定的主题。默认主题“bootstrap”，其他则需要联网，本地有网络连接也是可以显示的。

```markdown
[gimmick:themechooser](Theme)
 
[gimmick:theme](flatly)
```

- 创建“config.json”
    - "useSideMenu" 启用边栏导航栏
    - "additionalFooterText" 添加脚注信息，这里只是在原有的基础上添加，可以留空。默认的脚注信息可以在“index.html”中搜索修改
    -  "title" 页面“title”可以在“index.html”中设置
    -  "anchorCharacter" 在鼠标滑过标题时显示的信息

```json
{
        "useSideMenu": true,
        "additionalFooterText": "© 2015  ",
        "title": "my_wiki",
        "anchorCharacter": "#"
}
```

## 站内链接

添加“linux”目录，在设置站内链接时，**站内链接**使用`[](#!linux/linux_1.md)`

## 侧边导航栏

侧边导航栏显示所有二级标题，如果文章中只有一个二级标题则不会显示

## 添加[↑ TOP]到页面底部

锚点连接站内链接

```
<div align="right">**[↑ TOP](#if-then语句)**</div>
```
## 添加“上一节”“下一节”链接

```
<table>
<tr>
<td align="center">**[上一节](#!linux/linux_11.md)**</td>
<td align="center">**[下一节](#!linux/linux_13.md)**</td>
</tr>
</table>
```

参考：

- [MDwiki 使用手册](http://www.grdtechs.com/mdwiki/#!index.md)
- [MDwiki Quick Start](http://dynalon.github.io/mdwiki/#!quickstart.md)


---

<div align="right">**[↑ TOP](#搭建本地“MDwiki”)**</div>
