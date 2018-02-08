# 部署hexo



## 准备工作

[hexo中文文档](https://hexo.io/zh-cn/docs/index.html)

- **必要应用**:
  - `git`
  - `node.js`

- 安装`git`

```bash
$ sudo apt-get install git-core
```

- 安装`node.js`

```bash
$ curl https://raw.github.com/creationix/nvm/master/install.sh | sh
$ nvm install stable
```

> `nvm`---`node.js`的最佳安装方式(便于管理版本)

- 安装hexo

```bash
# 使用淘宝npm镜像
$ npm --registry https://registry.npm.taobao.org install express
#安装
$ npm install -g hexo-cli
```

具体安装也可以使用“--registry”选项：

> `npm --registry=https://registry.npm.taobao.org install package`

> `npm`是`node.js`的包管理工具("Node Package Manager"), 安装`node.js`成功后也已安装

- 安装deploy插件

```bash
$ npm install hexo-deployer-git --save
# 能够使用“hexo d” 发布文章的插件
```

## hexo建站

```bash
$ hexo init my_site	# 初始化一个本地项目
$ tree my_site/ -L  1 	# 查看初始化后的项目目录
my_site/
├── _config.yml
├── node_modules
├── package.json
├── package-lock.json
├── scaffolds
├── source
└── themes
$ cd my_site
(my_site) $ npm install		# 安装必要包
(my_site) $ hexo server		# 启动本地服务
```

- coding准备
  1. coding初始化一个`{username}.coding.me`
  2. 添加`SSH_key`
  3. 复制仓库`SSH`地址: `git@coding.net:{username}/{username}.coding.me.git`

- 修改`_config.yml`

```bash
# my_site/
deploy:
  type: git
  repo: git@coding.net:{username}/{username}.coding.me.git
  baranch: master
```

- 初始化仓库

```bash
$ git init
Initialized empty Git repository in /home/alex/my_site/.git/
$ git add .    # add 后面的”.“号，添加仓库内所有文件
$ git commit -m "initial commit"
```

> hexo文档并未提及要git初始化一个仓库

## 部署hexo

```bash
$ hexo g		# 生成静态网(generate)
$ hexo d		# 部署(deploy)
INFO  Deploying: git
...snip...
INFO  Deploy done: git
```

- 主题

> 喜欢[Next](https://github.com/iissnan/hexo-theme-next)主题的目录效果, 还有简介的界面, 还有详细的部署[文档](http://theme-next.iissnan.com/getting-started.html)

- 下载主题

```bash 
# my_site/
$ mkdir themes/next
$ curl -s https://api.github.com/repos/iissnan/hexo-theme-next/releases/latest | grep tarball_url | cut -d '"' -f 4 | wget -i - -O- | tar -zx -C themes/next --strip-components=1
$ rm -rf themes/lanscape/
```

- 修改`_config.yml`

```
<!-- my_site/_config.yml-->
titile: T.F's notes
author: T.F
url: https:/jzztf.coding.me
theme: next	# 将next主题命名为"next"置于"themes"目录下
```

- 生成页面

```bash
# my_site/
$ hexo new page tags    # 创建tags页面，next主题的tags页面会自动根据文章头信息生成标签云
$ hexo new page categories    # 创建categories页面，next主题的categories页面会根据文章头信息自动分类
$ hexo new page about    # 创建about页面
```
分别在生成的“tags“和”categories“目录下的”index.md“的头信息中添加`type： ”tags“`和`type: "categories"`

- tags


```markdown
my_site/source/tags/index.md
---
title: tags
date: 2017-09-02 10:46:34
type: "tags"
---
```
- categories

```markdown
my_site/source/categories/index.md
---
title: categories
date: 2017-09-02 10:46:49
type: "categories"
---
```

- 修改`post`模板

```markdown
my_site/scaffolds/post.md
---
title: {{ title }}
date: {{ date }}
tags:
categories:
---
```

> `scaffolds`目录下的`post.md`是文章模板，在执行`hexo new [article]`时创建的文章模板基于此模板

- 添加头像

```
<!--/my_site/themes/next/_config.yml-->
avastar: /images/avatar.png
```
> 在相应位置放置图标和图片

## 备份hexo（创建hexo分支）

```bash
# my_site/
$ git remote add origin [git@...]
$ git checkout -b hexo
Switched to a new branch 'hexo'
$ git branch
* hexo
 master
$ git add .
The following paths are ignored by one of your .gitignore files:
db.json
node_modules
public
Use -f if you really want to add them.
$ git commit -m "update site"
On branch hexo
nothing to commit, working directory clean
$ git push origin hexo
Counting objects: 435, done.
...snip...
* [new branch]      hexo -> hexo
```

> hexo 分支用来备份；master 分支用来部署

## 写作发布流程

> 在hexo分支下

```bash
# my_site/
$ hexo new "Deploy Hexo to Coding"    # 创建新文章
$ atom source/_post/Deploy-Hexo-to-Coding.md    # 编辑新文章
$ git add .    # 添加修改到仓库
$ git commit -m "add Deploy-Hexo-to-Coding.md"    # 提交修改到仓库
$ git push origin hexo    # 推送hexo分支到云端
$ hexo g    # 生成静态文件
$ hexo d    # 发布master分支到云端
```

## 换电脑后操作

> 只安装必要应用，不需要`hexo init`

```bash
# my_site/
$ git clone [git@...]
# 安装必要应用“git”，”node“，”hexo“和”deploy插件“
$ git checkout hexo  # 要先检出hexo分支
$ npm --registry=https://registry.npm.taobao.org install   
# 安装必要应用,这里使用的“--registry选项”，正常应该为“npm install” 
$ hexo s    # 查看运行情况
# 之后可以使用”写作发布流程“
```
