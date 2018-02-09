
# sed&gawk

## 初识sed

sed---stream editor(流编辑器)，自动格式化、插入、修改和删除文本元素等的简单命令行编辑器

操作内容：

- 一次从输入读取一行
- 根据所提供的编辑器命令匹配数据
- 按照命令修改数据流中的数据（只修改流中的数据，原数据不变）
- 将新的数据输出到STDOUT

语法：

`sed option script file`

选项|描述
:-:|:-
-e script|在处理输入时，将script中指定的命令添加到已有命令中去
-f file |在处理输入时，将file中指定的命令添加到已有命令中去
-n|不产生命令输出，使用print命令输出

- 命令行数据替换
```bash
$ echo "This is test" | sed 's/test/big test/'
This is big test
# "s"命令使得斜线指定的第二个字符串替换掉斜线指定的第一个字符串
```

## sed替换命令(s--substitude)

### 替换标记

- 数字 ==> 替换第n处匹配文本
- `g` ==> 全局替换
- `p` ==> 表明原先行要打印出来
- `w` ==> 将替换写入文本

实例：

- 数字

```bash
sed 's/dog/cat/2'  data # 将文件data中的第二处dog替换成cat
```

- `g`

```bash
sed 's/dog/cat/2'  data # 将文件data中的全部dog替换成cat
```
- `p`

```bash
sed -n 's/dog/cat/p' data
# '-n'选项禁止输出
# ‘p’选项使得原先行打印出来
# 组合使用就是禁止原先行打印，只输出修改后的行
$ cat data
A cat is running!
A dog is sitting!
$ sed 's/dog/cat/p' data  # 原先行要打印出来
A cat is running!
A cat is sitting!
A cat is sitting!
$ sed -n 's/dog/cat/p' data  # 只输出修改后的行
A cat is sitting!
```

- `w`

```bash
$ sed 's/dog/cat/ data_1' data
# 只输出修改后的数据行，等同于 "sed -n 's/dog/cat/p' data", 只是将输出写入到文件中
```

> 注意：
> 如果需要替换的字符中多”/“，使用起来会造成困惑，可以使用感叹号来做字符串分隔符，比如：`sed s!/bin/bash!/bin/csh! /etc/passwd`


### 常见替换场景 

- 文件中数据替换

```bash
$ cat data
A cat is running!
A dog is sitting!
$ sed 's/dog/cat/' data
A cat is running!
A cat is sitting!
# data 是一个文件，sed命令替换掉了流数据中的信息
```

- 多个命令同时执行替换

```bash
$ sed -e 's/dog/cat/;s/running/sitting/' data  #在命令行使用多个命令时，使用’-e‘选项
A cat is sitting!
A cat is sitting!
# 使用分号，可以执行多个命令
$ sed -e 's/dog/cat/
> s/running/sitting/
> ' data
A cat is sitting!
A cat is sitting!
# 单引号开头，一行输入一个命令，进行多命令输入
```

- 使用命令脚本替换

```bash
$ cat change.sed
s/dog/cat/
s/running/sitting/
$ sed -f change.sed data
A cat is sitting!
A cat is sitting!
# "-f"选项，使用sed脚本文件处理数据。sed脚本文件使用“sed”结尾便于识别
```

### 使用地址寻行

两种寻行模式

- 以数字形式（类似vim中语法）
- 以文本模式（正则表达式）

实例：

- 以数字形式寻行

```bash
$ sed '2s/dog/cat/' data  #替换第2行匹配数据
$ sed '2,4s/dog/cat/' data  # 替换第2行到第4行匹配数据
$ sed '2,$s/dog/cat/' data  # 替换第2行到文件结尾匹配数据
```

- 文本模式寻行

使用正斜线”//“将匹配模式包围起来

```bash
$ sed '/dog/s/dog/cat/' data # 替换包含dog的行的匹配数据
# 多行命令
$ sed '{
> /dog/s/dog/cat/
> /cat/s/cat/dog/
> }' data
A dog is running!
A dog is sitting!
# 单引号命令内也可加数字寻行
```

### 多命令组合


```bash
$ sed -e 's/dog/cat/; s/blue/red/' data  # 方法1: 使用’-e'选项，单引号内多个命令使用分号隔开
$ sed '{  # 方法2: 使用大括号，将多个命令括起来，分行显示；也可以在一组命令之前指定一个地址区间（寻址）
s/dog/cat/
s/blue/red/
}' data
```

## sed删除行

- 使用行寻址删除特定行（之删除数据流中的行，并不改变原数据)

```bash
$ sed '1d' data  # 删除第1行
A dog is sitting!
$ sed '2d' data  # 删除第2行
A cat is running!
$ sed '1,2d' data  # 删除前两行
A cat is running!
$ cat data # 原文件
A cat is running!
A dog is sitting!
```

- 使用文本模式删除特定行

```bash
$ sed '/number 1/d' data_2  # 文本寻行模式，包含'number 1'的行都删除
$ sed '/1/,/3/d' data_2  # 包含'1'的行开始到包含'3'的行结束，这之间行都删除
# 如果以上命令，/1/再次匹配到行，但是匹配不到/3/的行，就是没有匹配到结束模式，那之后的行都要被删掉
```

## sed插入附加文本

插入和附加

- `i` ==> insert，在匹配行之后加入
- `a` ==> append，在匹配行之前加入

语法：

```bash
sed '[address]command\
new line'
# '\'符号用于换行，如果只是一句话可以“sed '[address]command new line'”
```

实例：

```bash
$ sed '2a\ new line' data
A cat is running!
A dog is sitting!
new line
# 如果要插入多行，可换行
$ sed '2a\  # 数字寻址
line 1\
line 2' data
A cat is running!
A dog is sitting!
line 1
line 2
$ sed '/cat/a\  # 文本模式寻址
> new line' data
A cat is running!
new line
A dog is sitting!
```
## sed修改行

修改（change）行，`c`命令允许修改数据流中整行文本的内容，使用机制同插入附加文本命令相似

```bash
$ sed '2c\  # 数字寻址
> line 2' data
A cat is running!
line 2
$ sed '/dog/c\  # 文本模式寻址
> dog line' data
A cat is running!
dog line
```

## sed转换命令

转换命令（y）将斜线中对用的单个字符全部替换

```bash
$ sed 'y/dcrs/DCRS/' data
A Cat iS Running!
A Dog iS Sitting!
```

## sed打印命令

- `p` ==> 打印文本行
- `=` ==> 打印行号
- `l` ==> 列出数据流中中的文本和不可打印的ASCII字符

`p`命令一般与`-n`选项一起用，只显示修改后的行；`l`命令也可以呵`-n`选项一起用，只显示带有ASCII字符的行，而不显示原有行

```bash
$ sed -n 'l' data
A cat is running!$
A dog is sitting!$
```

`=`命令用来显示行号

```bash
$ sed '=' data
1
A cat is running!
2
A dog is sitting!
# 也可使用相应的寻址
$ sed '2=' data  # 数字寻址
A cat is running!
2
A dog is sitting!
$ sed '/dog/=' data  # 文本模式寻址
A cat is running!
2
A dog is sitting!
```
## 使用sed处理文件

### 写入文件

`[address]w filename`

写入命令允许将文件中特定行写入某一文件中

```bash
$ sed '1w data_3' data # 将文件data第一行写入文件data_3，不希望有输出，可以添加‘-n’选项
A cat is running!
A dog is sitting!
$ cat data_3
A cat is running!
```

### 读取文件

`[address]r filename`

读取命令允许从文件中读取数据，加入到数据流中显示，将指定文件中的内容插入到文件中

```bash
$ sed  '1r data' data_3 # 将data中的数据读取到data_3的第一行之后
A cat is running!
A cat is running!
A dog is sitting!
```
### 一个很酷的应用

```bash
$ sed '/LIST/{
> r name_list
> d
> }' notice.std
would the following people:
john
li
susan
wang
please report to the ship's captain.
$ cat notice.std  # 模板文件
would the following people:
LIST
please report to the ship's captain.
$ cat name_list  # 名单文件
john
li
susan
wang
```
模板文件将”LIST“放置在名单位置，然后使用sed命令将名单读取到”LIST“之后行，然后调用命令`d`删除”LIST“

> sed命令主要是两方面，一个是找到合适的位置（寻址），然后再执行其他命令

# 初识gawk

gawk提供了一个类编程环境来修改和重新组织文件中的数据，通常可以用来：

- 定义变量，保存数据
- 使用算术和字符串操作符来处理数据
- 使用结构化编程概念来为数据处理增加处理逻辑
- 通过提取数据中的数据元素，将其重新排列或格式化，生成格式化报告

## gawk命令格式

语法：

`gawk option program file`

选项|描述
:-:|:-
-F fs|指定行中划分数据字段的字段分隔符
-f file|从指定的文件中读取程序
-v var=value|定义gawk程序中的一个变量及默认值
-mf N|指定要处理的数据文件中的最大字段数
-mr N|指定数据文件中最大行数
-w keyword|指定gawk的兼容模式或警告等级

## gawk从命令行读取程序脚本

gawk从命令行读取脚本，用一个花括号来定义

`$ gawk '{print "hello world"}'`

## gawk使用数据字段变量

gawk的主要特性之一就是给每一行数据每个数据元素分配一个字段变量

- $0 代表整行数据
- $1 代表第1个数据元素
- $2 代表第2个数据元素
- $n 代表第n个数据元素

每个数据元素，默认是任意空白字符来划分的，当然也可以使用选项”-F“来指定，比如：


`gawk -F: ‘{print $1}’ /etc/passwd`

## gawk在程序脚本中使用多个命令

```bash
$ echo "my name is john" | gawk '{$4=li; print $0}'
my name is li
```

## gawk 从文件中读取程序

```bash
$ cat script.gawk
{print $1 "'s home directory is " $6}
$ gawk -F: -f script.gawk  /etc/passwd
root's home diretory is /root
```
为避免混淆脚本，可以为gawk脚本设定后缀名

## gawk在处理数据前和后运行

数据处理前后处理数据，在命令前后加上"BEGIN"&"END"

`gawk -F: 'BEGIN{print Hello}'`
`gawk -F: 'END{print Goodbye}'`

## 应用

```bash
$ cat script.gawk
BEGIN{
print  "the latest list of users and shells"
print "UserID \t Shell"
print"------- \t -------"
FS=":"
}

{
print $1 "       \t " $7
}

END{
print "this concluds the listings"
}
$ gawk -f script.gawk /etc/passwd
the latest list of users and shells
UserID 	 Shell
------- 	 -------
root       	 /bin/bash
...snip...
alex       	 /bin/bash
zalex       	 /bin/bash
this concluds the listings
```

