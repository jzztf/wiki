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


---

<div align="right">**[↑ TOP](#命令行参数)**</div>

<table>
<tr>
<td align="center">**[上一节](#!linux/linux_shell/linux_13.md)**</td>
<td align="center">**[下一节](#!linux/linux_shell/linux_15.md)**</td>
</tr>
</table>
