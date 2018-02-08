# Python Manage Files

## python文件目录

> 获得当前目录，创建新目录，改变目录，返回绝对目录，判断绝对目录

```python
>>> import os
>>> os.getcwd()  # 获得当前目录
'/home/alex/Desktop'
>>> os.makedirs('/home/alex/Desktop/ex')  # 创建新目录
>>> os.getcwd()
'/home/alex/Desktop'
>>> os.chdir('/home/alex/Desktop/ex')  # 改变目录
>>> os.getcwd()
'/home/alex/Desktop/ex'
>>> os.path.abspath('..')  # 返回绝对目录
'/home/alex/Desktop'
>>> os.path.isabs('/home/alex/Desktop')  # 判断绝对目录
True
>>> os.path.isabs('.')
False
```

## 两个路径之间关系os.path.relpath(path, start)

```python
>>> os.path.relpath('/home/alex/Desktop/ex', '/')
'home/alex/Desktop/ex'
>>> os.getcwd()
'/home/alex/Desktop/ex'
```

## 目录名称和基本名称，分解路径

```python
>>> os.path.dirname('/home/alex/Desktop/ex')  # 目录名称
'/home/alex/Desktop'
>>> os.path.basename('/home/alex/Desktop/ex')  # 基本名称
'ex'
>>> os.path.split('/home/alex/Desktop/ex')  # 分解路径
('/home/alex/Desktop', 'ex')
>>> '/home/alex/Desktop/ex'.split(os.path.sep)  # 分解路径为列表
['', 'home', 'alex', 'Desktop', 'ex']
```

## 目录名称和基本名称，合成路径

```python
>>> import os
>>> os.path.join('/home/alex/Desktop/test', 'write.md')
'/home/alex/Desktop/test/write.md'
```

## 列出文件，获得文件大小

```python
>>> os.listdir('/home/alex/Desktop/ex')  # 列出目录文件
['ex.md']
>>> os.getcwd()
'/home/alex/Desktop/ex'
>>> os.path.getsize('/home/alex/Desktop/ex/ex.md')  # 获得文件大小
14
```

## 检测路径和文件

```python
>>> os.path.exists('/home/alex/Desktop/ex')  # 检测路径
True
>>> os.path.exists('/home/alex/Desktop/ex/ex')
False
>>> os.path.isfile('/home/alex/Desktop/ex')  # 检测文件
False
>>> os.path.isfile('/home/alex/Desktop/ex/ex.md')
True
>>> os.path.isdir('/home/alex/Desktop/ex')
True
>>> os.path.isdir('/home/alex/Desktop/ex/ex.md')
False
```

## python 中写入读取文件

```python
>>> file = open('ex.md', 'w')  # 以'w'写入方式打开一个文件
>>> file.write('Hello World!')  # 写入内容
12
>>> file.close()  # 关闭文件
>>> file = open('ex.md', 'a')  # 以'a'添加模式打开文件
>>> file.write('\nHello again!\n')  # write不会添加换行符号，自行添加
14
>>> file.close()
>>> file = open('ex.md')
>>> file_content = file.read()  # 读取内容
>>> print(file_content)
Hello World!
Hello again!
```

> 用shelve保存变量和pprint.pformat保存变量

## shelve模块

> 适用对象：整型，浮点型，字符串，列表，字典

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')  # shelve.open()打开文件
>>> cats = ['pooka', 'zophie', 'simon']
>>> shelfFile['cats'] = cats  # 写入文件
>>> shelfFile.close()  # 关闭
>>> shelfFile = shelve.open('mydata')  # 需要调用前，再次打开
>>> shelfFile['cats']  # 直接当作字典一样调用键对应的值
['pooka', 'zophie', 'simon']
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile.close()
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())  # 所有键列表
['cats']
>>> list(shelfFile.values())  # 值列表
[['pooka', 'zophie', 'simon']]
>>> shelfFile.close()
```

## pprint.pformat保存变量

> 可将代码返回成更易阅读的代码，同时符合python规范，可用此方法，编写自己的模块

```python
>>> import pprint
>>> cats = [{'name': 'zophie', 'desc': 'chubby'},\
{'name': 'pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)  # pprint.pformat返回一个列表
"[{'desc': 'chubby', 'name': 'zophie'}, {'desc': 'fluffy', 'name': 'pooka'}]"
>>> file = open('myCats.py', 'w')
>>> file.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> file.close()
>>> import myCats
>>> myCats.cats
[{'desc': 'chubby', 'name': 'zophie'}, {'desc': 'fluffy', 'name': 'pooka'}]
>>> myCats.cats[0]
{'desc': 'chubby', 'name': 'zophie'}
>>> myCats.cats[1]
{'desc': 'fluffy', 'name': 'pooka'}
>>> myCats.cats[0]['name']
'zophie'
```

> python组织文件

## shutil模块：在python对文件进行复制移动改名删除

```python
>>> import shutil
>>> shutil.copy('test.md', '/home/alex/Desktop/test1')  # shutil复制
'/home/alex/Desktop/test1/test.md'
>>> shutil.copy('/home/alex/Desktop/test1/test.md', '/home/alex/Desktop/test2/test2.md')
>>> shutil.move('/home/alex/Desktop/test1/test1.md', '/home/alex/Desktop/test2/test1.md')  # shutil移动
'/home/alex/Desktop/test2/test1.md'
>>> shutil.rmtree('/home/alex/Desktop/test1')  # shutil删除文件夹
```

## os模块的删除文件和文件夹命令

```python
>>> os.unlink('/home/alex/Desktop/test2/test1.md')  # os删除文件
>>> os.rmdir('/home/alex/Desktop/test2')  # os删除目录，文件夹必须为空
```

## send2trash的保险删除

```python
>>> import send2trash  # pip install send2trash
>>> send2trash.send2trash('test.md')
```

## 迭代遍历循环目录

```python
>>> for folderName, subfolders, filenames in os.walk('/home/alex/Desktop/test'):
...     print('The current folder is ' + folderName)
...     for subfolder in subfolders:
...             print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
...     for filename in filenames:
...             print('FILE INSIDE ' + folderName + ': ' + filename)
...     print('')
```

> zip压缩，查看，解压

## 压缩文件

```python
>>> newzip = zipfile.ZipFile('new.zip', 'w')  # 打开新zip文件
>>> newzip.write('test.md', compress_type= zipfile.ZIP_DEFLATED)  # 写入文件，以某参数方式写入
>>> newzip.close()  # 关闭zip文件
>>> zipfile = zipfile.ZipFile('new.zip')  # 查看zip压缩文件01步
>>> zipfile.namelist()  # 查看zip压缩文件02步
['test.md']
```

## 获取压缩文件信息

```python
>>> zipinfo = zipfile.getinfo('test.md')  # 获取压缩文件信息01步
>>> zipinfo.file_size  # 获取压缩（原）文件信息02步
0
>>> zipinfo.compress_size  # 获取压缩文件压缩后大小
2
>>> zipfile.close()  # 关闭压缩文件
```

## 解压压缩文件

```python
>>> zipextra = zipfile.ZipFile('new.zip')  # 解压文件01步
>>> zipextra.extractall()  # 解压文件02步（解压缩有）
>>> zipfile.close()  # 关闭压缩文件
>>> zipextra.extract('test.md')  # 解压某一文件
'/home/alex/Desktop/test.md'
>>> zip_extra.extract('test.md', '/home/alex/Desktop/test0')  # 解压某一文件到某路径
'/home/alex/Desktop/test0/test.md'
>>> zip_extra.close()  # 关闭压缩文件
```

---
<div align="right">**[↑ TOP](#python文件目录)**</div>
