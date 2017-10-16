# linux函数

## if

### 语法：

```bash
if command
then
    command
fi
```
### 变体

- if-then省略

```bash
if command;then
    command
fi
```
- if-then-else

```bash
if command
then
    command
else
    command
fi
```
- if-then嵌套

```bash
if command
then
    command
else
    if command
    then
        command
    fi
fi
```
- elif

```bash
if command
then
    command
elif command
then
    command
fi
``` 

### 判断

- test语句

```bash
if test [condition]
then
    command
fi
```

- "[ ]"方括号代替test

```bash
if [ condition ]
then
    command
fi
```
### 三种判断

- 数值比较
  - 方法：[ n1 -eq n2 ];
  - '-eq'='equal';
  - ‘-ge’=‘greater equal’;
  - '-gt'='greater than';
  - '-le'='less equal';
  - '-lt'='less than'

- 字符串比较
  - 方法：[ str1 = str2 ]或[-n str1]
  - [ -n str1 ]:字符串为“非0”
  - [ -z str1 ]:字符串为“0”
  - [ str1 = str2 ]  字符串完全一样
  - [ str1 != str2 ] 字符串不匹配
  - [ str1 > str2 ] ASCII码排序，如果数值比较直接使用“>”符号，会被系统当做字符串排序
  - [ str1 < str2 ] ASCII码排序

- 文件比较
  - [ -e file ] 检查文件是否存在
  - -d 检查文件是否存在并且是目录文件
  - -f 检查文件是否存在并且是一个文件
  - -r-w-x 检查文件是否可读-可写-可执行
  - -s 检查文件是否为非空
  - -O-G 检查文件时是否存在并属于当前用户-属于当前默认组
  - -nt-ot 检查文件新旧，‘newer than’和‘older than’

### 复合条件测试

- `[ condition1 ] && [ condition2 ]`
- `[ condition1 ] || [condition2]`

### if-then高级特性

- 双括号用于数学表达式，包括(`val++后加;val--后减;++val先加;--val先减;!逻辑取反;~位求反;**幂;<<左位移;>>右位移;&布尔和;|布尔或;&&逻辑和;||逻辑或`)

```bash
if ((expression))
then
    command
fi
```

- 双方括号用于高级字符串处理,可以使用正则表达式

```bash
if [[ expression ]]
then
    command
fi
```

## case

> case 为每个变量可能会有不同的值提供选项

```bash
case variable in
    pattern1) command;;
    pattern2 | pattern3) command;;
    *) command;;
esac  # case 翻过来
```

## for

> 用于遍历列表

### 语法：

```bash
for var in list
do
    command
done
```

### 变体

```bash
for var in list; do command
done
```

## while

> while命令看起来像是if-then和for的结合体，要进行条件测试，然后进行循环。

语法：

```bash
while test command
do
    command
done
```
中断循环

- break命令

> break命令直接退出循环

- continue命令

> continue命令暂时退出循环，一旦遇到合适的条件会继续下去


参考：

- [结构化命令](#!linux/linux_shell/linux_12.md)
- [更多结构化命令](#!linux/linux_shell/linux_13.md)

---


<div align="right">**[↑ TOP](#if)**</div>
