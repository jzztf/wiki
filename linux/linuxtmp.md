# linux 一些小技巧

## 创建临时文件/临时文件夹

使用`mktemp`命令

- 创建临时文件

```bash
$ mktemp tmp.xxx
```

- 在`/tmp`创建临时文件

```bash
$ mktemp -t temp.xxx
$ mktemp  # 会在/tmp自动创建一个临时文件
```

- 创建临时目录

```bash
$ mktemp -d dir.xxx
$ mktemp -d  # 会在/tmp自动创建一个临时文件目录
```
