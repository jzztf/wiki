# linux命令行与shell编程_第14章

> 处理用户输入

在运行脚本时，需要与使用者进行交互，此时就需要获得用户输入，通常可以通过命令行参数，命令行选项以及直接从键盘读取输入的方法

## 命令行参数

命令行参数允许在运行脚本时向命令行添加数据

### 读取参数

bash shell将位置参数(positional parameter)分配给命令行中的所有参数，在脚本中可以像使用其他变量一样使用位置参数变量

参数|名称
:-|:-
$0|程序名
$1|第一个参数
$2|第二个参数
$n|第n个参数
$9|第九个参数
${10}|第十个参数
${m}|第m个参数

注意：

- 命令行参数包含空格，需要用引号(单或双)引起来
- 需要10个以上参数，可以使花括号`${10}`

### 读取脚本名

在运行脚本时，如果使用的是脚本的整个路径，那么$0就是脚本的整个路径，此时如果需要剥离脚本名，可以使用basename命令，比如：

```bash
#!/bin/bash

name=$(basename $0)
echo
echo The script name is $name
```

### 测试参数

使用者可能会忘掉或多加参数，所以在脚本中要测试参数是否有效保证脚本能够正常运行，比如：


```bash
#!/bin/bash

if [ -n $1 ]
then
    echo hello $1
else
    echo please add parameter
fi
```

##  特殊参数变量

特殊的参数变量包括：

参数变量|意义
:-|:-
$#|参数的个数
$*|参数的所有数据，被当做列表对待
$@|参数的所有数据，被当做一个整体来对待


### 参数总数`$#`

参数的总数，可以用来测试参数数量上是否正确


```bash
#!/bin/bash
if [ $# -ne 2 ]
then
    echo Usage test.sh a b
else
    echo good！
fi
```

注意：

- 如果想使用${$#}表示最后一个参数，或出现错误，因为花括号内不能使用美元符号，可以替换成感叹号，使用${!#}表示最后一个参数

### 作为一个整体的`$*`和`$@`

- $*将所有参数当做一个整体来处理
- $@将所有的参数当做一个整体，但是可以处理每一个参数，可以使用for循环遍历每一个参数

## 移动变量

在不知道有多少个参数的情况下，可以使用`shift`命令，移动参数，配合while循环，每次都是处理第一个参数。


```bash
#!/bin/bash

count=1
while [ -n $1 ]
do
    echo "Parameter #$count = $1"
    count=$[ $count + 1 ]
    shift  # 移除一个参数
done
```
注意：

- 当然`shift`命令也可以一次移动多个位置，只需指明需要移动的位数，`shift 2`就是移动两个参数的位置

## 处理选项

“选项”是跟在单破折号后的单个字母

### 查找选项

#### 处理简单选项

使用`case`命令处理对应的选项

```bash
#!/bin/bash

echo
while [ -n "$1" ]
do
    case "$1" in
        -a) echo "Found -a";;
        -b) echo "Found -b";;
        *) echo "Not Found!";;
    esac
    shift
done
```
#### 分离参数和选项

bash shell会用双破折号线(--)表明选项列表结束，检测双破折号线只需在`case`命令中添加一项即可

```bash
#!/bin/bash

echo
while [ -n "$1" ]
do
    case "$1" in
        -a) echo "Found -a";;
        -b) echo "Found -b";;
        --）shift
            break;;   退出循环
         *) echo "$1 is not an option!";;
    esac
    shift  # 将双破折号移出
done
```

### 处理带值的选项
 
`$ ./test.sh -a test -b -c test2`

```bash
#!/bin/bash
echo
while [ -n "$1" ]
do
    case "$1" in
        -a) echo "Found -a";;
        -b) param="$2"
	    echo "Found -b, param: $2"
	    shift;; # 因为while循环中只有一个shift，这里多加一个踢出参数
	-c) echo "Found -c";;
        --) shift
            break;;
        *) echo "$1 is not an option";;
    esac
    shift
done
```

### getopt

> getopt命令可以接受一系列任意形式的命令选项和参数，并将他们转成适当的格式。

#### 命令行中使用getopt

语法：

- `getopt optstring parameter`

实例：

- `getopt ab:cd -a -b test -cd test2 test3`

注意：

- 在需要参数的选项后面添加冒号，以便于后面识别。在使用getopt时，可以将参数合在一块使用比如`-ab`
- 如果命令中出现了‘optstring’中没有的选项则会报出错误，需要忽略错误的话可以使用`-q`选项，比如`getopt -q -ab test`

#### 脚本中使用getopt

> 主要在于使用`set`命令
> `set`命令有一个双破折号选项会将命令行参数替换成`set`命令的命令行值，也就是一个替换的的功能，将shell中的命令行参数交给set命令双破折线之后的命令处理

比如在脚本中使用：

- `set -- $(getopt -q ab:cd "$@")`

注意：

- 仍然有一个问题，就是`getopt`无法处理一个带有空格的参数，下面需要使用高级一点的工具`getopts`

### getopts

> getopt将命令行上的选项和参数处理后只生成一个输出，而getopts命令一次只处理命令行上检测到的一个参数，处理完后返回状态码“0”.如果选项需要有个参数值可以加一个冒号，如果不希望有错误输出，可以再“optstring”之前添加冒号。

> getopts命令会用到两个环境变量，如果一个选项需要参数值，`OPTARG`环境比那辆就会保存住那个值，`OPTIND`环境变量保存了参数列表中getopts正在处理的参数的位置，这样就能处理其他命令行参数了

实例：

```bash
#!/bin/bash
#
echo
while getopts :ab:cd opt
do
  case "$opt" in 
    a) echo "Found -a";;
    b) echo "Found -b, with value $OPTARG";;
    c) echo "Found -c";;
    *) echo "Unknown option: $opt";;
  esac
done
```

注意：

- getopts命令解析命令行选项时会移除选项开头的单破折线，所以在case命令中不需要使用破折线。
- getopts优点
  - 参数值值中可以加空格
  - 选项字母和参数放在一起使用
  - 命令行中所有未定义的选项统一输出成问号
- getopts命令在处理每个选项时，会将`OPTIND`环境变量值增一，在getopts完成处理选项时可以使用shift和`OPTIND`值来移动参数，要处理参数时，可以将前面处理的都移开再处理，使用`shift $[ $OPTARG - 1 ]`。

## 将选项标准化

常用的linux命令选项

选项|描述
:-|:-
-a|显示所有对象
-c|指定一个目录
-e|扩展一个对象
-f|指定读入数据的文件
-h|显示命令的帮助信息
-i|忽略文本大小写
-l|产生输出的长格式版本
-n|使用非交互模式（批处理）
-o|将所有输出重定向到指定输出文件
-q|以安静的模式运行
-r|递归地处理目录和文件
-s|以安静的模式运行
-v|生成详细输出
-x|排除某个对象
-y|对所有问题回答yes

## 获得用户输入

### 基本读取

> read命令从标准输入(键盘)或者一个文件描述符中获取输入，收到输入将其存入一个变量中

- `-p`选项

允许read命令指定提示符，比如`read ”Password： “ pass`

- `-n`选项

允许read命令不会在字符串末尾添加换行符使得用户紧跟其后输入数据

### 超时

> 添加`-t`选项设置read命令等待时间

```bash
#!/bin/bash

if read -t 5 -p "Enter something: " message
then
        echo "this is $message"
else
        echo
        echo "timeout!"
fi
```
### 隐藏方式读取

> 添加`-s`选项，显示器上看不到，实际上是颜色被设置成背景色一样的颜色了

```bash
#!/bin/bash

read -s -p "Enter your password: " pass
echo
echo "Is your password really $pass?"
```

### 从文件读取

> 可以使用read命令读取文件中的数据，可以使用cat命令,将结果通过管道直接传给含有read命令的while命令

```bash
#!/bin/bash

count=1
cat test | while read line  # 将每一行读取的内容赋值给line变量
do
   echo "Line $count: $line"
   count=$[ $count + 1 ]
done
echo "Finished!!"
```

---

<div align="right">**[↑ TOP](#命令行参数)**</div>

<table>
<tr>
<td align="center">**[上一节](#!linux/linux_shell/linux_13.md)**</td>
<td align="center">**[下一节](#!linux/linux_shell/linux_15.md)**</td>
</tr>
</table>
