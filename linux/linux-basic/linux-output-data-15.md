# linux命令行与shell编程_第15章

> 呈现数据

## 理解输入和输出

- 标准文件描述符

linux用文件描述符“file descriptor”来识别每个文件对象

|  代码  |  描述  |
| :--: | :--: |
|  0   | 标准输入 |
|  1   | 标准输出 |
|  2   | 标准错误 |

- 重定向错误
  - `command 2> file`就是将命令错误信息定向到文件
  - `command &> file`就是将文件的正确错误信息都定向到文件

## 在脚本中重定向输出

- 临时重定向

如果有意使脚本生成错误信息，可以单独一行输出到STDERR。可以使用输出重定向符将输出信息重定向到STDERR文件描述符，在重定向到文件描述符时，必须在文件描述符数字之间添加“&”

```bash
echo “this is error” >&2 
```
这样只有在使用错误输出重定向时才会显示出来。

```bash
#!/bin/bash

echo "this is error" >&2
echo "normal message"
```

正常输出

```bash
$ ./test.sh 
this is error
normal message
```

使用输出重定向输出错误时

```bash
$ ./test.sh 2> file
$ cat file
$ this is error
```

- 永久重定向

exec命令可以使shell在脚本执行期间重定向到某个特定的文件描述符

```bash
exec 1> file # 所有的正确输出都会输出到文件file
exec 2> fileerror # 脚本中一旦使用此命令，该脚本所有的错误输出都会输出到fileerror
```

## 在脚本中重定向输入

exec命令允许将STDIN重定向到linux上的文件中

`exec 0< file`

实例：

```bash
#!/bin/bash

exec 0< file

count=1

while read line
do
    echo "LINE #$count: $line"
    count=$[ $count + 1 ]
done
```

## 创建自己的重定向

### 创建输出文件描述符

```bash
#!/bin/bash

exec 3>test

echo "normal message"
echo "test message" >&3
echo "normal message"
```

正常语句都会输出到屏幕上，经过自定义的输出会输出到特定文件test中

### 重定向文件描述符

> 恢复已重定向的文件描述符，可以分配另外一个文件描述符给标准文件描述符，再重新将标准文件描述符传给另外一个文件描述符

```bash
#!/bin/bash

exec 3>&1
exec 1>testout

echo "This should store in the outfile"
echo "along with this line"

exec 1<&3

echo "Now things should be back"
# 运行之后
$ ./test.sh
This should store in the outfile
along with this line
$ cat testout
Now things should be back
```

以上脚本完成了以下几个步骤

- `exec 3>&1`将文件描述符3重定向到文件描述符1，也就是STDOUT，意味着任何发送给文件描述符3的内容都会发到显示器上
- `exec 1>testout`将文件描述符1也就是STDOUT重定向到文件testout，将应该在显示器上显示的内容存储到文件testout中
- `exec 1>&3`将文件描述符1中定向到文件描述符3，在完成一些重定向后，脚本将文件描述符重定向到3的位置也就是1的位置，恢复了之前的重定向

> 以上用法类似于`IFS.OLD=IFS`之后使用`IFS=IFS.OLD`

### 创建输入文件描述符

```bash
#!/bin/bash

exec 6<&0
exec 0< testfile

count=1
while read line
do
    echo "Line #$count: $line"
    count=$[ $count + 1 ]
done
exec 0<&6
read -p "Are you done now?" answer
case $anwser in
  Y|y) echo "goodbye"
  N|n) echo "sorry, this is the end"
esac
```
以上脚本说明：

- `exec 6<&0` 将0重定向到6
- `exec 0< testfile` testfile传到0就相当于传到了6，将testfile作为输入
- `exec 0<&6` 又将6传到了0，恢复重定向之前的状态，等待键盘输入

### 创建读写文件描述符

```bash
#!/bin/bash

exec 3<> testfile
read line <&3
echo "Read: $line"
echo "This is a test line" >&3

$ cat testfile
first line
second line
third line
$ ./test.sh
Read:first line
$ cat testfile
first line
This is a test line
second line
```
exec命令将文件描述符3分配给testfile进行读写，read命令读取了testfile的第一行，指针指向第二行数据，之后的echo语句将内容写入到3中，也就是使testfile中，所以后来testfile中第二行被覆盖。

### 关闭文件描述符

使用特殊符号`&-`关闭之前文件描述符

```bash
#!/bin/bash

exec 3>testfile

echo "this should be in testfile" >&3

exec 3>&-

echo "this should not be in testfile" >&3
```

## 列出打开文件描述符

`lsof`命令可以显示当前系统上打开文件的每个文件的信息，包括后台运行的所有进程以及登录的所有用户。

- `-p`选项可以指定进程ID
- `-d`选项允许指定要显示的文件描述符编号
- 要知道进程当前的PID，可以使用特殊环境变量$$
- `-a`选项可以两个选项结果执行布尔AND操作

```bash
 ~ lsof -a -p $$ -d 0,1,2

COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
zsh     4752  ztf    0u   CHR  136,2      0t0    5 /dev/pts/2
zsh     4752  ztf    1u   CHR  136,2      0t0    5 /dev/pts/2
zsh     4752  ztf    2u   CHR  136,2      0t0    5 /dev/pts/2
```

## 阻止命令输出

将命令输出重定向到`/dev/null`

## 创建临时文件

`/tmp`文件专供临时文件使用，linux会在系统启动时删除其中的文件，而且在此目录中，每个用户都有读写的权限。

另外专用的命令“mktemp”可以在`/tmp`创建属于当前用户的文件，只有当前文件可以进行读写。

### 创建本地临时文件

```bash
$ mktemp tmp.xxxx
```

### 在/tmp目录创建临时文件

```bash
$ mktemp -t tmp.xxxx
```

- `-t`选项会强制`mktemp`命令在`/tmp`目录下创建临时文件

### 创建临时目录

```bash
$ mktemp -d dir.xxx
```

- `-d`选项会创建一个临时目录

## 记录消息

> tee 命令相当于一个“T”接口，可以将命令重定向到某个文件的同时也输出到电脑屏幕上

- `-a`选项使得tee命令重定向到文件时是以添加的模式

```bash
$ date | tee testfile
$ who | tee -a testfile
```

## 实例



---

<div align="right">**[↑ TOP](#title?)**</div>

<table>
<tr>
<td align="center">**[上一节](#!linux/linux_shell/linux_?.md)**</td>
<td align="center">**[下一节](#!linux/linux_shell/linux_?.md)**</td>
</tr>
</table>
