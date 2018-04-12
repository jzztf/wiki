# 基本shell命令

## 文件和目录列表

### `ls`查看目录

常用参数:
- `-F` ==> 区分目录,目录后会有`/`
- `-R` ==> 递归选项,深入目录,列出目录中的文件
- `-l` ==> 显示长列表,长列表包含的基本信息
  - 示例: `drwxr-xr-x   3 ztf ztf 4.0K 3月   7 14:05 Desktop`
  - 文件类型,`d`==>目录;`-`==>文件;`c`==>字符文件;'b'==>块设备
  - 文件权限
  - 硬链接总数
  - 属主用户名
  - 属组用户名
  - 文件大小以字节为单位
  - 上次修改时间
  - 文件名会目录名
- 使用通配符过滤输出列表
  - `?` ==> 代表一个字符
  - `*` ==> 代表零个或任意多个字符
  - `[]` ==> 字符选取范围
  - `[!]` ==> 不包含某字符

### `tree`优雅查看目录

- 安装
  - `sudo apt-get install tree`
- 参数
  - `-a`列出所有文件
  - `-d`列出所有目录
  - `-f`列出完整路径
  - `-L level`深入level级别的目录
  - `-P pattern`列出满足pattern的文件
  - `-I pattern`不列出满足pattern的文件
  - `--ignore-case`忽略大小写
  - `--matchdirs`pattern匹配时匹配文件夹
  - `--noreport`不生成最后报告
  - `--filelimit #`当文件总数超过#时不列出目录
  - `--timefmt <f>`按照指定格式<f>打印时间
  - `-o filename`将结果输出到文件
- 更多参数`tree --help`

### `touch`创建文件

-`touch filename`创建文件
- 查看访问时间`ls -l --time=atime filename`

### `cp`复制文件

- `cp /path/file /path2/file2`将path路径下的file复制到path2下
  - `-i`参数可以使增加系统询问,避免覆盖同名文件
  - 当复制目录时,可添加`/`使得目的更明确
  - `-R`递归赋值整个目录内容
  - `cp`命令也可以使用通配符
  - 在使用目录时,可以使用制表键`tab`进行命令补全

### 链接文件

链接是目录中指向文件真实位置的占位符

- 硬链接:内容完全相同的两个文件
- 软链接(符号链接):仅仅是一个指向文件

```bash
$ ls -li link_file*
7078952 -rw-rw-r-- 2 ztf ztf 0 3月  12 17:53 link_file
7078952 -rw-rw-r-- 2 ztf ztf 0 3月  12 17:53 link_file_hard
7079175 lrwxrwxrwx 1 ztf ztf 9 3月  12 17:56 link_file_soft -> link_file
# 2是1的硬链接,二者有相同的incode;
# 3是1的软连接,也就是符号链接,其本身大小仅为9个字节,包含了指向源文件的链接
```
注意:
- 硬链接适用于同一存储设备;不同存储媒体之间只能使用软链接

### `mv`移动或重命名文件

```
mv source destination
# 将source移动到destination
mv file file2
# 将file重命名为file2
```

常用参数:
- `-i`增加问询,防止覆盖同名文件

### 处理目录

- 创建目录:
  - `mkdir new_dir`
  - 参数`-p`根据需要创建确实父目录
- 删除目录
  - `rmdir new_dir`只删除空目录
  - `rm`命令,使用参数`-r`递归删除
  - 使用参数`-f`避免问询
  - 最危险的操作`rm -rf *`

### 查看文件

- 查看文件类型
  - `file filename`
- 查看整个文件
  - `cat filename`
  - 参数:
    - `-n`带上行号
    - `-b`为有文本的内容加上行号
    - `-T`不让制表符出现
  - `more filename`分页查看文件
  - `less filename`高级的"more",源自"less is more"
  - `tail filename`默认查看文件尾部10行内容
    - `tail -n # filename`查看末尾#行内容
    - `-f`选项允许在其它进程动态查看文件尾部状态,是观察系统日志的绝佳工具
  - `head -# filename`查看文件开头#行内容

