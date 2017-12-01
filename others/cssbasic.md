# css


## 基础

### 使用css的三种方式

- 内联
   `<head><style>css</style></head>`
- 外联
   `<link rel="stylesheet" type="text/css" href="main.css">`
- 行内
   `<p style="color: red; font-size: 24px;"></p>`
### 声明&选择器

#### 声明

```css
p {color: red; font-size: 24px;}
/*大括号内的为声明块；“color: red:为声明”*/
```
#### 选择器

##### 元素选择器

```css
html: <p></p> | css: p {声明}"
```

##### 选择器分组

```css
h1, h2 {声明}
/*所有h1和h2*/
```

##### 类选择器

```css
html: class="class | css: .class {声明}"
```

##### id选择器

```css
html: id= "id" | css: #id {声明}
```

##### 子选择器

```css
ul>li {声明}
/*父元素为ul的所有li*/
```

##### 后代选择器

```css
body p {声明}
/*body下的所有p*/
```

##### 兄弟选择器

```css
p+img {声明}
/*紧挨着p之后的所有img*/
```

##### 伪类选择器

```css
：link | :hover | :focus | :active | :visited
```

##### 属性选择器

- “[]”用法：p[class]，所有有class属性的
- “[=]”用法：p[class="dog"]，所有有值为dog的class
- “[]”用法：p[class]，所有有class属性的
- “[~]”用法：p[class~="dog"]，所有有class属性的值中有空格+dog的
- “[^]”用法：p[attr^"d"]，所有值为d开头的
- “[$]”用法：p[attr$"d"]，所有值为d结尾的
- “[*]”用法：p[attr*"d"]，所有值包含d的

### @import

用法：@import url(""); 在主css文件中引入其他css


## 颜色

### 颜色表达
#### rgb

`rgb(255, 255, 255)`
最基本的颜色表达：rgb=(red green blue);数值范围0-255.

#### hex十六进制

`#ffffff`
rgb的十六进制表达法：两位一组表达0-255的值

#### 颜色名字

`red`
网页支持的颜色名称很多

#### hsl&hsla

`hsl(0° 0% 100%) 或者 hsla(0° 0% 100% 0.5)`

- hue-色相
  众颜色分布在一个圆盘上按角度取色
- saturation-饱和度
  值越大，灰色越少，颜色越亮
- lightness-明度
  值越大，黑色越少，颜色越白
- opacity-模糊度
  可以结合hsl一起使用; 也可以当作单独属性使用”opacity:  ;“;取值0-1
### 颜色使用分类

- 前景色: `color：red；`
- 背景色: `background-color: grey;`

## 文本

### font-family
- serif
  - 带小尾巴的字体
  - Georigia, Times, Times New Roman
  - 用法：font-family：Georigia, sans-serif; 如果没有第一种字体会从第二种字体中选一个
- sans-serif
  - 尾部较直
  - Arial, Verdana,Helvetica
- monospace
  - 字母宽度相同，多用于代码
  - Courier, Courier New
- curisive
  - 手写体
  - Comic Sans MS,Monotype Corsiva
- fantasy
  - 装饰字体，一般用于标题
  - Impact
### font-face
- 用法：@font-face { }；旨在引入字体，之后便可使用
- 从其他网站下载字体使用，速度较慢
- 两个属性：font-family： ""；src: url {'xx.eot'}
- 字体格式：xx.eot |xx.woff |xx.ttf/otf | xx.svg
- 如果使用字体较多，可使用如上顺序；不同浏览器支持的格式不同

### font-size
- 用法：font-size: 24px;
- 单位：px； %； em

### font-weight
- 用法：font-weight: bold;
- 值：normal | bold

### font-style
- 用法：font-style: italic;
- 值：normal | italic | oblique
- italic=斜体；obique=倾斜

### text-transform
- 用法：text-transform: upercase;
- 值：uppercase | lowercase | capitalize

### text-decoration
- 用法：text-decoration: underline;
- 值：none | underline | overline | line-through | blink(难用)

### line-height
- 用法：line-height: 1.4em;
- 值：最好用em；1.4-1.5合适

### letter-spacing&word-spacing
- 用法：letter-spacing: 0.5em | word-spacing: 0.5em;
- 值：一般单词之间距离为0.25em

### text-align
- 用法：text-align: left;
- 值：left | right | center | justify
- justify：段落中除了最后一行，其他都两头对齐

### vertical-align
- 用法：vertical-align: top;
- 值：baseline | sub | super | top | text-top | middle | bottom | text-bottom
- 多用于引入图片时的对齐

### text-indent
- 用法：text-indent: 10px;
- 值：px， em
- 也可以使用负值将元素放到页面边缘

### text-shadow
- 用法：text-shadow: 1px 1px 0px #000000;
- 值：几个值分别表示阴影水平，垂直的相对位置，模糊度，颜色

### 伪类:first-letter;:first-line
- p:first-line { color: red;}

### 伪类:link;:visited
- 用法：a:link { color: red;}
- :link表示未访问的链接；：visited表示已经访问过的链接

### 伪类:hover;:active;focus:
- 用法：a:hover { color: red}
- :hover表示鼠标滑过时；:active表示控件被激活时；:focus表示焦点在时
- 如果结合:link&:visited一起使用按照l-v-h-f-a的顺序

## 盒模型

### 基础:css将所有的元素放在一个盒子box里
### width&height
- 用法: width: 10px;
- 值：px | em | %

### min-width&max-width | min-height&max-height
- 用法：max-width：200px；
- 旨在当浏览器变化时，一些元素不会太长或太短; 不会太宽也不会重叠

### overflow
- 用法：overflow：hidden
- 值：hidden | scroll
- overflow在内容与box盒模型冲突时，决定内容的显示方式

### border，padding&margin

- 由内至外padding-border-margin
- border
  - border-width
    - 用法：border-width: thick;
    - 值：thin | medium | thick；
    - 当然也可以分别设置border-top-width；border-right-width等
  - border-style
    - 用法：border-style：solid
    - 值：solid | dotted | dashed | double | groove | ridge | inset | outset | hidden/none
    - 当然也可以对四个边界分别设定border-top-style; border-bottom-style等
  - border-color
    - 用法：border-color: red
    - 值：颜色的值
  - 当然也可以对四边界设定border-top-color; border-right-color等
  - border
    - 用法：border: 2px solid red;
    - 对border的三个属性一同设置
  - border-image
    - 用法：border-image： url() 10 10 10 10 stretch;
    - 值：url()图片位置；10-10哪里切割；stretch 
    - stretch | repeat | round三个值表明图片是要被拉伸还是重复还是包围
  - border-shadow
    - 用法：border-shadow: 1px 2px 3px red; 
    - 值：几个值分别表示阴影水平，垂直的相对位置，模糊度，颜色
  - 边界圆角
    - 用法：radius：10px；
    - 10px表示圆角半径为10px；当然也可以进行分别设定比如border-top-right-radius: 10px；等
- padding
  - 如果宽度width给定了，padding就会加在盒模型的宽度上
  - 用法：padding: 2px 2px 2px 2px;
  - 也可以分别设定padding值，padding-top,padding-bottom等
- margin
  - 用法：margin: 1px 1px 1px 1px;
  - 通常也可以使用两个值margin: 10px 20px;表示上下和左右
  - 也可以分别设定margin-top, margin-right等；
  - 内容居中可以设定宽度，然后margin：10px auto 10px auto;

### 改变元素块级/行内
- 用法：display：inline；
- 值：inline | block | inline-block | none
- inline-block使得块级元素想行内元素一样浮动有利于创建多区块

### 隐藏元素
- 用法：visibility: hidden;
- 值：hidden | visible
- 元素可以被隐藏，但是会占一个位

## 列表，表格，表单

### 列表
- 列表类型list-style-type
  - 用法：list-style-type：decimal；
  - 无序列表的值：none | disc | circle | square
  - 有序列表的值：decimal | decimal-leading-zero | upper-alpha | lower-alpha | upper-roman | lower-roma
- 列表图像list-style-image
  - 用法：list-style-image: url();
  - 该属性可用于元素ul和li
- 列表位置list-style-position
  - 用法：list-style-position: outside;
  - 值：outside | inside
  - 表示列表前的提示符在行内还是行外
- list-style
  - 用法：list-style: circle inside;

### 表格
- width：设定表格的宽度
- padding：设定表格内容与单元格的空间
- firefox：background-image: -moz-linear-gradient(#336666,\n#66cccc);
  - 并不是所有的浏览器都支持
  - chrome：background-image: -webkit-linear-gradient(#336666,\n#66cccc);text-transform：设定表头大写
- letter-spacing&font-size：设定更多的格式
- border-top&border-bottom：设定上下边界
- text-align：可以设定单元格内内容的对齐方式
- background-color：表格背景颜色
- :hover ：设定鼠标滑过时的变化
- empty-cell
  - 用法：empty-cells: show;
- 值：show | hide | inherit
  - 决定是否显示表格
- border-spacing&border-collapse
- border-spacing: 5px 10px;分别表示水平方向和垂直方向
- border-collapse: collapse;将单元格的边界合并成无缝隙状态

### 表单
- input
  - 可以应用font-size | color | background-color | background-image | border-radius | :focus | :hover设定input元素
  - 设定字体大小 | 字体颜色 | 背景色 | 背景图片 | 边界圆角弧度 | 输入框在聚焦时 | 鼠标滑过时的状态
- submit
  - 可以应用color | text-shadow | border-bottom | background-color | :hover 设定submit元素
  - 设定 颜色 | 文字阴影 | 底部边界 | 背景色 | 鼠标滑过时的状态
- fieldsets&legends（表单元素分组）
  - 可以应用color | background-color | border | border-radius | padding
  - 设定 颜色 | 背景色 | 边界 | 边界弧度 | 内边界
- cursor
  - 用法：cursor: crosshair
  - 值：auto | crosshair | default | pointer | move | text | wait | help |url("cursor.gif")
  - 默认为文字标 | 十字架 | 文字标 | 指向 | 文字标 |等待 | 帮助 | 自定义图标

## 布局

### position
- normal flow正常的工作流
  - 每一个块级元素依次往下排
- relative position
  - 在正常工作流下，进行位置的设置
  - 用法：position：relative;
  - 位置表示：top: 10px; bottom: 10px; right: 10px; left: 10px;
- absolute position
  - 离开了正常工作流，相对于页面进行设置
  - 用法：position: absolute;
  - 位置表示：top: 10px; bottom: 10px; right: 10px; left: 10px;
- fixed position
  - absolute position的一种；相对于窗口，停留在某一位置不动
  - 用法：position: fixed;
  - 位置表示：top: 10px; bottom: 10px; right: 10px; left: 10px;
- z-index
  - 当使用以上位置是会出现重叠的时候，显示的时间会不同；如果要保持在上，可以使用z-index
  - 用法：z-index：5；
  - 值为阿拉伯数字，值越小越接近顶部

### float
- 浮动和位置能达样的效果
  - 用法：width：200px; float: left;
- clear
  - 用法：clear: left
  - 值：left | right | both | none
  - 意义在于不跟着前面的元素浮动，回到正常工作流
- overflow
  - 用法：overflow: auto;
  - 如果页面都是浮动元素，浏览器会忽略这些元素的大小;使用overflow使其容器不在浮动
- inline-block
  - 解决上面的问题；使用display:inline-lock也可以解决
- fixed-layout&liquid-layout
  - 一个使用计算的方式布局；一个使用百分比布局，各有优略

### html5
- `<header>`
  - 头信息
- `<nav>`
  - 导航栏
- `<article>`
  - 主体
- `<aside>`
  - 边栏
- `<footer>`
  - 页脚
- `<section>`
  - 不同的区块
- `<hgroup>`
  - 将不同级别的标题组合到一起，低级别的做副标题
- `<hgroup><h1></h1><h2></h2></hgroup>`
- `<figure>&<figcaption>`
  - 用于图片添加解释
- `<figure><img src="路径" alt="说明"><figcaption></figcaption></figure>`

## 图像

### 图像大小
- 用法：width: 200px; height: 300px;
### 图像位置
- float：left
- display: block; margin: 0px auto;

### 背景图
- 引入背景
  - background-image: url("images/x.png")
- 背景重复
  - background-repeat: repeat
  - 值：repeat | no-repeat | repeat-x | repeat-y
- 背景移动
  - background-attachment: scroll;
  - 值：fixed | scroll
- 背景位置
  - background-position: top left
  - 值： left top | left center | left bottom | center top | center center | center bottom | right left | right center | right bottom
- background
  - background: grey url("images/bg.png") no-repeat fixed left top;
  - 值顺序：background-color | background-image | background-repeat | background-attachment | background-position
- 颜色渐变
  - firefox：background-image: -moz-linear-gradient(#336666,\n#66cccc);
  - 并不是所有的浏览器都支持
  - chrome：background-image: -webkit-linear-gradient(#336666,\n#66cccc);



[思维导图](http://naotu.baidu.com/file/02cc78ad4a1078a158b01e862cafa7f0?token=e3ec376cd66ac8c7)
![CSS.png](http://upload-images.jianshu.io/upload_images/6540347-25ffa1e252f76fa7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)