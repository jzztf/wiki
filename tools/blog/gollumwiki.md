# Gollum Wiki


## github初始化wiki

在wiki页面创建页面home，复制下wiki地址，本地克隆下来

## 安装gollum

> **[gollum](https://github.com/gollum/gollum)**
> **[markdown](https://daringfireball.net/projects/markdown/syntax)**

```bash
$ [sudo] gem install gollum
```

## 启动gollumwiki

```bash
$ cd wiki
$ gollum
# open 'http://localhost:4567'
```
然后就可以在浏览器中创建编辑页面并修改。

githubwiki的好处在于每一次修改都可以看得见 

---
## 页面标题

默认页面的标题就是文件路径，本页面标题“gollum manual”，对应路径“/gollum-manual”

### 通过`CLI`设置标题

在命令行使用`gollum --h1-title`启动gollum，页面中第一个`h1`标题会被用做页面标题。选项会覆盖元数据语法。

```markdown
# 这是页面标题
# 这是页面“内容”标题
```

### 通过元数据语法设置标题

语法：

`<!-- --- title: 页面标题-->`

注意：元数据语法必须放在页面最开头部分

### 子页面

- 头文件命名为`_Header.ext`
- 边栏文件命名为`_Sidebar.ext`
- 页脚文件命名为`_Footer.ext`

## 页面安全

因为安全和其他原因，gollum页面不包含`CSS`，`JavaScript`和某些`HTML`复杂的标记

### 标签

语法：

`[[tag]]`

标签也接受被管道符分隔的特征标记，比如：

- `[[前特征|标签]]`
- `[[标签|后特征]]`

### 标签链接

标签链接，可以通过点击链接连接到某些资源

- `[[链接]]`：直接显示链接
- `[[链接文字|链接]]`：点击链接文字连接到某些资源

### 链接到外部资源

- `[[http://example.com]]`
- `[[链接文字|http://example.com/pdfs/gollum.pdf]]`

### 链接到内部文件

链接必须是路径

- 相对路径`docs/diagram.png`
- 绝对路径`/docs/diagram.png`,指向`gollum`仓库的根目录

### 链接到内部图片

1. `[[图像url|alt=文字说明]]`
    - 如果图像找不到，就显示文字说明
2. `[[图像url|frame]]`
    - 图像被放在一个框架中
3. `[[图像url|align=position]]`
    - 默认图像放置在左边，“position”可以被替换为`left`，`center`和`right`
4. `[[图像url|float]]`
    - `float`选项使得文字包围图像，不支持`align=center`
5. `[[图像url|height=value]]`
    - 设置图像高度最大值，`value`替换值必须是`px`或`ex`结尾
6. `[[图像url|width=value]]`
    - 设置图像宽度最大值，`value`替换值必须是`px`或`ex`结尾

- 注意1： 所有的特征都可以通过管道符连接同时使用
    - 比如： `[[图像url|frame|alt=文字说明]]`
- 注意2： 默认情况文字将会填满图片周边所有空间，如果要开始新的空白行，使用`[[_]]`

### 链接内部页面

下面的标签将创建一个指向`gollum`页面

`[[规范-页面-文件名]]`

注意：

- 不使用插件
- `spaces`空格要被`-`替换
    - `[[gollum manual]]`将会指向`gollum-manual.ext`页面
- `forward slashes`正斜线要被`-`替换
    - `[[movies/the hobbit]]`将会指向`movies-the-hobbbit.ext`页面

指向的页面可以放在`git`仓库任意位置，`gollum`会自行寻找

### 包裹标签

不同于链接到标签，下面的语法，将一个标签嵌入到另一个

`[[include:标准-页面-文件名]]`

### 目录标签（TOC=Table-of-content）

`[[\_TOC_]]`

或者定义其最大宽度

`[[\_TOC_|levels = 3]]`

注意：

- 该语法对于识别大小写字母，务必使用大写字母
- 它也可以被插入到子标签中
- `TOC`也有一个全局化设置，可以嵌入到所有页面中
    - `Precious::App.set(wiki_options, {:universal_toc => true})`

## 注释标签

在标签前加单引号“'”

`'[[标签]]`

## 代码块

```
\```
代码区
\```
```

## 语法高亮

```
\```bash
添加语言类型
\```
```

## MACROS(巨指令)

## Default Macros

## AllPages

- 描述：列出所有wiki页面
- 语法：`<<\AllPages()>>`
- 举例：`<url id="pages">AllPagesMacroPage<li></li></url>`

## GlobalTOC

- 描述：列出可点击的`TOC`
- 语法：`<<\GlobalTOC()>>`
- 举例：`<<\GlobalTOC(AllPages)>>`

## Custom Macros

???

## DIAGRAMS

- [[Sequence diagrams|https://www.websequencediagrams.com/]]在线流程图

- [[PlantUML diagrams|https://github.com/gollum/gollum/wiki/Custom-PlantUML-Server]]???

## MATHEMATICS

[[MATHEMATICS|https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference]]???

## Authentication

[[omnigollum|https://github.com/arr2036/omnigollum]]???