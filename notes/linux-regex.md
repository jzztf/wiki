# linux 正则表达式

正则表达式是通过正则表达式引擎实现的，linux中有两种流行正则表达式引擎：

- POSIX基础正则表达式(Basic Regular Expression, BRE)
- POXIS扩展正则表达式(Extended Regular Expression, ERE)

# 基础正则表达式

## 纯文本

```bash
$ sed ‘/dog/s/red/black/’ data  # 匹配包含“dog”的行，将行内“red”替换成“black”
A red cat is running!
A black dog is sitting!
$ cat data
A red cat is running!
A red dog is sitting!
```

## 特殊字符

`.*[]^$\+?|()`这些符号在正则表达式中都有特殊含义，如果在匹配模式中作为符号使用，需要添加转义符`\`

```bash
$ sed -n '/\/root/s/\/bin\/bash/\/bin\/zsh/p' /etc/passwd
root:x:0:0:root:/root:/bin/zsh
```

## 锚字符

### `^`脱字符

只有放在匹配模式行首才能作为匹配行首的字符，否则只能当作一个普通字符来处理

```bash
$ cat data
A ^Red cat is running!
Red dog is sitting!
$ sed -n '/^Red/p' data
Red dog is sitting!
$ sed -n '/ ^Red/p' data
A ^Red cat is running!
```

### `$`

锁定在行尾

```bash
$ sed -n '/!$/p' data
A ^Red cat is running!
Red dog is sitting!
```

### 组合使用

通常用来过滤空白行

```bash
$ sed '/^$/d' data
```

## 点号字符

`.`号字符匹配换行符之外任意单个字符

```bash
$ sed -n '/.ti/p' data
Red dog is sitting!
```

## 字符组

`[]`方括号来定义字符组，匹配方括号内任意一个字符

```bash
$ sed -n '/[s].[r]/p' data
A ^Red cat is running!
```

## 排除型字符组

`^[]`方括号外添加`^`脱字符排除方括号内单个字符

## 区间

`[a-z]`,`[0-9]`,`[A-Z]`指定区间

## 特殊字符组

BRE特殊字符组
组|描述
:-:|:-
[[:alpha:]]|
[[:alnum:]]|
[[:blank:]]|
[[:digit:]]|
[[:lower:]]|
[[:print:]]|
[[:puntct:]]|
[[:space:]]|
[[:upper:]]|








## 区间
## 特殊字符组合

# 扩展正则表达式
## 问号
## 加号
## 花括号
## 管道符号
## 表达式分组


# 应用
## 目录文件计数
## 电话号码
## 邮件地址
