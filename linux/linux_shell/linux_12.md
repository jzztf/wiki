# linux命令行与shell编程_第12章

> 使用结构化命令——"if-then"语句

## if-then语句

语法：

```bash
if <command>
then
    <commands>
fi
```

或者

```bash
if <command>;then
    <commands>
fi
```

> "if"语句会运行"if"之后那个"command"，如果该命令退出出状态码为"0"，则位于"then"之后的"commands"命令会被执行

## if-then-else

语法：

```bash
if <command>
then
    <commands>
else
    <commands>
fi
```
> 如果"if"之后那个"command"退出状态码为"0"则执行"then"之后的"commands"；否则则执行"else"之后的"commands"

## 嵌套if

> "if"语句的多重嵌套，嵌套的"if-then"语句位于"if-then-else"语句的"esle"命令中

语法：

```bash
if <command>
then
    <commands>
else
    if <command2>
    then
        <commands>
    fi
fi
```

或者也可以使用"elif"语句使代码更清晰

```bash
if <command1>
then
    <commands>
elif <command2>
then
    <more commands>
fi
```

## test命令

> 原始"if"命令只能判断"if"之后命令退出状态码为"0"和非"0"的状态，如果要判断其他条件则可以使用"test"命令，命令格式`test condition`

语法：

```bash
if test <condition>
then
    <commands>
fi
```

或者使用方括号代替"test"命令

```bash
if [ condition ]  # 注意：方括号两边要留空
then
    <commands>
fi
```

### test命令可以判断的三类条件

- 数值比较
- 字符串比较
- 文件比较

### 数值比较

比较|描述
:-|:-
n1 -eq n2|n1=n2 ?
n1 -ge n2|n1>=n2 ?
n1 -gt n2|n1>n2 ?
n1 -le n2|n1<n2 ?
n1 -lt n2|n1<n2 ?

### 字符串比较

> 字符串之间的比较，主要分为两个字符串完全一样、两个字符串不一样、字符串组成字母符号的排序和字符串是否为空。字符串之间排序">"和"<"需要使用转义符"\"转义。

比较|描述
:-|:-
str1 = str2|两字符串相等
str1 != str2|两字符串不相等
str1 < str2|字符串1排在字符串2之后
str1 > str2|字符串1排在字符串2之前
-n str1|字符串为非"0"
-z str1|字符串为"0"

> 注意： 如果数值比较时使用了标准数学比较符，会被当做字符串处理；字符串比较使用的是ASCII码排序

### 文件比较

比较   |描述
:------|:-----
-e file|检查文件是否存在
-d file|检查文件是否存在并是一个目录
-f file|检查文件是否存在并是一个文件
-r file|检查文件是否存在并可读
-w file|检查文件是否存在并可写
-x file|检查文件是否存在并可执行
-s file|检查文件是否存在并非空
-O file|检查文件是否存在并属当前用户所有
-G file|检查文件是否存在并且默认组与当前用户相同
file1 -nt file2|检查文件1是否比文件2新
file1 -ot file2|检查文件1是否比文件2旧

## 复合条件测试

- `[ condition1 ] && [ condition2 ]` 逻辑与
- `[ condition1 ] || [ condition2 ]` 逻辑或

## if-then高级特性

-可用于数学表达式的双括号
-可用于高级字符串处理的双方括号

### 双括号

语法：

```bash
if ((expression))  # expression可以是任意数学赋值或表达式
then
    <commands>
fi
```

符号|描述
:----|:----
val++|后增
val--|后减
++val|先增
--val|先减
!|逻辑取反
~|位求反
**|幂运算
<<|左位移
>>|右位移
&|位布尔和
&#124;|位布尔或
&&|逻辑和
&#124;&#124;|逻辑或

### 双方括号

语法：

```
if [[expression]]
then
    <commands>
fi
```

双括号提供了“test”命令未提供的另一种特性——模式匹配，支持正则表达式。

## case特性

> "case"提供了一个更清晰的方法来为变量每个可能的值指定不同的选项

语法：

```bash
case variable in
    pattern1 | pattern2) <commands1>;;
    pattern3) <commands2>;;
    *) default <commands3>;;
esac
```

---

<div align="right">**[↑ TOP](#if-then语句)**</div>

<table>
<tr>
<td align="center">**[上一节](#!linux/linux_shell/linux_11.md)**</td>
<td align="center">**[下一节](#!linux/linux_shell/linux_13.md)**</td>
</tr>
</table>

