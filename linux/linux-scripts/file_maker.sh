#!/bin/bash

for (( a = 1; a <= 26; a++))
do
	touch linux_$a.md
	echo "# linux命令行与shell编程_第$a章" >> linux_$a.md
	cat file_tmp >> linux_$a.md
done


# file_tmp/
# 注释:[:11,22s/^/#/g];取消注释:[:11,22s/#//g]
#---
#
#<div align="right">**[↑ TOP](#title?)**</div>
#
#<table>
#<tr>
#<td align="center">**[上一节](#!linux/linux_shell/linux_?.md)**</td>
#<td align="center">**[下一节](#!linux/linux_shell/linux_?.md)**</td>
#</tr>
#</table>
