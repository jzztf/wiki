# linux命令行与shell编程_第13章

> 更多的结构化命令

## for循环命令

语法：

```bash
for var in list
do
    <commands>
done
```

或者

```bash
for var in list; do <commands>
done
```

> shell 列表：由空格分开的字符串，`ls`命令的结果也是列表

### 读取列表的值

> for命令最基本的用法就是遍历for循环命令自身所定义的一系列值

```bash
for test in A B C
do
    echo "$test"
done
```

for命令遍历列表时，他会将列表中的下个值赋给$test变量

### 读取列表的复杂值

> 单引号会引起读取列表错误

- 使用转义符将“单引号”转义
- 使用双引号来定义用到单引号的值或包含空格的值

实例：

```bash
for test in I don't know if this'll work
do
    echo "word: $test"
done
```

结果：

```bash
word: I
word: dont know if thisll
word: work
```

### 从变量读取列表

定义一个列表

```bash
list=“A B C D”
list=$list" E"  # 列表拼接
for test in $list
do
    echo "word: $test"
done
```

### 从命令读取值

```bash
for test in $(ls ~/)
do
    echo "$test"
done
```

### 更改分隔符

> 特殊的环境变量IFS--内部字段分隔符(internal field separator)

> 列表默认的字段分隔符是空格；制表符；换行符

如果需要限制或修改字段分隔符可以使用：

- `IFS=$'\n'只识别换行符`
- `IFS=$':'
- 要多个识别符可以拼在一块使用，`IFS=$'\n':;`

### 使用通配符读取目录

```bash
for file in ~/*  # 也可以使用多个目录
do
    echo "$file"  # 可能文件名包含空格，需要将变量用双引号括起来
done
```

## while语句

> while命令可以看做是if-then和for循环的合体；while命令允许定义一个要测试的命令，然后循环执行一组命令。

### 语法：

```bash
while test command
do
    command
done
```
### 使用多个测试命令

> 只要最后一个命令，退出状态码为“0”，后续的命令就会被执行

```bash
var=10
while echo “$var”
    [ $var -ge  0] # 多个命令测试，主要看最后一个命令
do
    echo "Inside the loop"
    var=$[ $var - 1 ]
done
```
    
## until语句

> until命令工作方式正好相反。取字面意思就是，达到那个临界条件，才会有后续的工作。

语法：

```bash
until test command
do
    command
done
```

实例：

```bash
#!/bin/bash
var=100

until [ $var -eq 0 ]
do
    echo $var0
    var=$[ $var - 25 ]
done
``` 

## 循环
### 嵌套循环

实例：

```bash
#!/bin/bash
for (( a = 1; a < 3; a++ ))
do
    echo "start loop $a"
    for (( b = 1; b <= 3; b++ ))
    do
        echo "inside loop $b"
    done
done
```
### 循环处理文件数据

- 使用嵌套循环
- 修改IFS环境变量

```bash
#!/bin/bash

IFS.OLD=$IFS  # 方便在需要恢复IFS本身的默认属性时，使用IFS=$IFS.OLD
IFS=$'\n'
for entry in $(cat /etc/passwd)
do
    echo "Value in entry -"
    IFS=:
    for value in $entry
    do
        echo "    $value"
    done
done
```

### 控制循环

#### break命令

> 在执行break命令时，它会跳出当前执行的循环

#### continue命令

>continue命令在终止循环时并不是真正的终止，它会在满足一定的循环条件时继续循环。

### 处理循环的输出

> 可以对循环的输出重定向

```bash
while command
do 
    command
done > output.txt
```
## 实例

### 查找可执行文件

> 创建for循环对$PATH目录进行迭代；使用内嵌循环迭代每一行内容，检测文件是否有可执行权限

```bash
#!/bin/bash

IFS=:
for folder in $PATH
do
    echo "$folder: "
    for file in $folder/*
    do
        if [ -x $file ]
        then
            echo "    $file"
        fi
    done
done
```

### 创建多个用户账户

> 创建多个用户,主要内容就是读取数据文件，将读取到的用户名添加到系统中去.创建文件“users.csv”,格式“userid，user name”.read -r选项保证读入的内容是原始内容;useradd -c选项添加备注到passwd备注栏中；-m选项自动创建用户登录目录.

```bash
#!/bin/bash
input="users.csv"
while IFS="," read -r userid name
do
        echo "Adding $userid"
        useradd -c "$name" -m $userid
done
```

---

<div align="right">**[↑ TOP](#for循环命令)**</div>

<table>
<tr>
<td align="center">**[上一节](#!linux/linux_shell/linux_12.md)**</td>
<td align="center">**[下一节](#!linux/linux_shell/linux_14.md)**</td>
</tr>
</table>

