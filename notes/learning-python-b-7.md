## 字符串

- 字符串常量
- 单双引号字符串是一样的

```python
>>> 'hello' == "hello"
True
```

- 用转义序列代表特殊字节
  - `\n`换行符
  - `\t`制表符
  - `\`忽视(连续)
  - `\'`单引号
  - `\"`双引号
  - `\a`响铃
  - `\b`倒退
  - `\f`换页
  - `\r`返回
  - `\v`垂直制表符
  - 等等
- raw字符串抑制转义

```python
>>> print(r"hello\n world")
hello\n world
>>> print("hello\n world")
hello
 world
```

- 三重引号编写多行字符串
  - 多行字符串
  - 多行注释


- 实际应用中的字符串

  - 基本操作

  - 索引和切片

    - 扩展str[I:J:K]
    - 切片每隔K个元素, 从I-J进行切片

    ```python
    >>> str = "abcdefg"
    >>> str[::-1]
    'gfedcba'
    >>> str[1:5]
    'bcde'
    # 复数对边界进行了反转
    >>> str[5:1:-1]
    'fedc'
    ```

  - 为什么要在意: 切片

    - 切片有很多应用场景,比如程序参数检测

  - 字符串转换工具

    - `str()`
    - `ord()`会将字符串转换为其对应的ASCII码
    - `chr()`会与上面函数执行相反的结果

  - 修改字符串

    - 字符串不可变性质,不能在原地进行修改,比如索引赋值就会引发错误
    - 但是可以使用合并,切片赋值给新的字符串来修改

    ```python
    >>> s = "hello world"
    # 原地赋值会失败
    >>> s[2] = 'L'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    # 切片合并重新赋值给新的变量是可以的
    >>> s = s[:2] + 'L' + s[3:]
    >>> s
    'heLlo world'
    # 也可以使用字符串方法实现
    >>> s.replace('eL','el')
    'hello world'
    # 格式化方法修改字符串,实际是生成了新的字符串
    >>> "hello %s"%('world!')
    'hello world!'
    >>> "hello {}".format('world!')
    'hello world!'
    ```

  - 字符串方法

    - [http://www.runoob.com/python/python-strings.html](url)

    ```python
    >>> s = "hello world"
    >>> dir(s) # 查看字符串方法
    ```

  - 实际应用中的常见字符串方法

  ```python
  s.startswith()
  s.endswith()
  s.isalpha()
  s.find()
  s.lstrip()
  s.rstrip()
  s.strip()
  s.center()
  s.count()
  ```

  - 字符串格式化表达式

  ```python
  >>> "hello %s"%('john')
  "hello john"
  ```

  - 更高级的用法

  ```python
  # 高级语法
  %[(name)][flags][width][.precision]tyecode
  # "(key_name)"列出字典的相应值
  >>> print('li: %(li)s'%{'li': 89, 'mei': 78})
  li: 89
  # "-N" => 空出N位空间左对齐
  >>> print('%-6s:\n%-6s:'%('name','age'))
  name  :
  age   :
  # "width" => 所占位数,宽度; 其实是一种右对齐
  >>> print('...%5d...'%(123))
  ...  123...
  >>> print('...%*d...'%(5,123))
  ...  123...
  >>> print('%-5s:%d\n%-5s:%d'%('john',89,'li',100))
  john :89
  li   :100
  >>> print('%-5s:%3d\n%-5s:%3d'%('john',89,'li',100))
  john : 89
  li   :100
  >>> print('%-5s:%4d\n%-5s:%4d'%('john',89,'li',100))
  john :  89
  li   : 100
  >>> print('%-5s:%*d\n%-5s:%*d'%('john',4,89,'li',4,100))
  john :  89
  li   : 100
  # ".precision" => 精确度
  >>> print('%.3f'%(1/3))
  0.333
  >>> print('%.*f'%(3,1/3))
  0.333

  ```

  ​

  ```python
  # 字符串格式化代码
  s => 字符串
  d => 十进制数
  i => 整数
  o => 八进制数
  x => 十六进制数
  % => 常量
  # 格式化可使浮点数的对齐和填充
  ```

  - ​
  - 基于字典的格式化调用

  ```python
  >>> "hello {}".format("john")
  "hello john"
  >>> "hello {0}{1}".format("john","!")
  "hello john!"
  ```

  ​

  - 字符串格式化调用方法

    - 基础知识
    - 添加键, 属性和偏移量

    ```python
    >>> "My {0} runs {1}".format('laptop','linux')
    'My laptop runs linux'
    >>> "My {0[1]} runs {1[sys]}".format(['laptop','PC'],{'sys':'linux',})
    'My PC runs linux'
    ```

    ​

    - 添加具体格式

    ```python
    # 在十个字符范围内左对齐,右对齐
    >>> '{0:10} = {1:>10}'.format('123','123')
    '123        =        123'
    >>> '{0:10} = {1:<10}'.format('123','123')
    '123        = 123       '
    ```

    ​

    - 与%格式化表达式比较
    - 为什么用新的格式化方法
    - 同样分类的类型共享其操作集合
    - 可变类型能够在原处修改

- 习题

  - python如何修改字符串
    - 字符串无法修改,只能通过一定的方法重新赋值