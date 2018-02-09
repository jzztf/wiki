#!/bin/bash
# 逐行读取数据，添加相应符号并写入到另一文件
# 用法：$ ./create_TOC.md test_file
# testfile中每个内容占一行；最后生成"test_file_TOC.md"文件

cat $1 | while read LINE
do
	echo "- [$LINE](#$LINE)" >> ./$1_TOC.md
done
