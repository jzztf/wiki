# 元组,文件及其他

- 常见元组常量

```python
()							=> 空元组
T = (0,)					=> 单元素元组
T = (o, 'Ni', 1.2, 3)		=> 多元素元组
T = o, 'Ni', 1.2, 3			=> 同上
T = ('abc', ('def', 'ghj'))	=> 嵌套元组
T = tuple('spam')			=> 构造器构造元组
T[i]						=> 索引
T[i][j]						=> 索引嵌套元素
T[i:j]						=> 切片
len(T)						=> 计算长度
T1 + T2						=> 拼接
T * 3						=> 重复
for x in T: print(x)		=> 迭代,遍历
'spam' in T					=> 判断
[x ** 2 for x in T]			=> 元组解析
T.index('Ni')				=> 搜索
T.count('Ni')				=> 计数
```

- 实际应用中的元组
  - 元组符号: 逗号和元括号
  - 转换,方法及不可变性
- 元组与列表
  - 元组可以看成简单的对象组合
  - 列表看成是随时间改变的数据结构
- 文件
- 常见文件运算

```python
output = open(r'/Documents', 'w')		=> 创建输出文件, 'w'以写入模式创建
input = open('data', 'r')				=> 创建输入文件, 'r'以只读模式创建
input= open('data')						=> 默认为只读
aString = input.read()					=> 把整个文件读成一个字符串
aString = input.read(N)					=> 读取N个字节组成一个字符串
aString = input.readline()				=> 读取一行组成一个字符串
aList = input.readlines()				=> 读取所有行组成一个字符串列表
output.write(aString)					=> 写入字符串到文件
output.writelines(aList)				=> 将字符串列表内所有文件写入字符串
output.close()							=> 关闭文件
output.flush()							=> 将输出缓冲区刷到硬盘中,但不关闭文件
anyFile.seek(N)							=> 修改文件位置偏移到N处
for line in open('data'): use line		=> 文件迭代器一行一行读取
open('f.txt', encoding='latin-1')		=> Unicode文本文件
open('f.bin','rb')						=> 二进制bytes文件
```

- 文件处理主要为以下操作

```python
file = open('/file.txt', 'w')
file = open(r'\file.txt', 'w')	# 如果是Windows文件路径需要使用原始字符串
file.readline()
file.readline(N)
file.readlines()
file.write()
file.close()
```



- 文件上下文管理器

```python
with open(r'/Documents/data.txt') as myfile:
    for line in myfile:
        ...use line here...
        
# 等价于==>

myfile = open(r'/Documents/data.txt')
try:
    for line in myfile:
        ...use line here...
    finally:
        myfile.close()
```

- 其他文件工具
  - 标准流,类似`sys.stdout`
  - os模块中的描述文件
  - sockets,pipes和FIFO文件
  - 通过键来获取文件
  - shell命令流`os.popen`
- 引用和拷贝
  - 使用copy模块`copy.deepcopy()`完整拷贝
  - 在修改一些对象时,以防止元数据被改,可进行复制,操作副本
- 比较相等性和真值
  - "=="测试相等性
  - "is"测试一致性