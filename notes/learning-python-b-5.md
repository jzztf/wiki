## 数字

- python数字类型的完整工具

  - 整数
  - 复数
  - 固定精度的十进制数
  - 有理分数
  - 集合
  - 布尔类型
  - 无穷的整数精度
  - 各种数字内置函数和模块

- 数字常量

  - 整数(正整数和负整数)
    - 允许使用十六进制,八进制和二进制常量来表示整数
    - 允许整数具有无穷精度,只要内存允许
  - 浮点数(带小数点的数)
  - 复数
  - 调用模块创建其他数字类型

- 内置数学工具和扩展

  - 表达式操作符`+,-,*,/,>>,&`
  - 内置数学函数`pow,abs,round,int,hex,bin`
  - 公用模块`random,math`

- python表达式操作符

  - 当数字和操作符结合时,python执行时将计算得到一个值
  - python中表达式是使用通常的数学符号和操作符号写出来的
  - Python表达式操作符及程序
    - `yield x`生成器函数发送协议
    - `lambda args:expression`生成匿名函数
    - `x if y else z`三元选择表达法
    - `x or y`逻辑或
    - `x and y`逻辑与
    - `not x`逻辑非
    - `x in y, x not in y`成员关系
    - `x is y, x is not y`对象实体测试
    - `x < y, x <= y, x >y, x >= y`大小比较
    - `x == y, x != y`相等性操作符
    - `x | y`位或,集合并集
    - `x ^ y`位异或,集合对称差
    - `x & y`位与,集合合集
    - `x << y, x >> y`左移或右移y位
    - `x + y, x - y`加法/合并,减法,集合差集
    - `x * y, x % y, x / y, x // y`乘法/重复,余数/格式化,除法:真除法或floor除法
    - `-x. +x`一元减法,识别
    - `~x`按位求补(取反)
    - `x ** y`幂运算
    - `x[i]`索引(序列,映射及其他)点号取属性运算,函数调用
    - `x[i:j:k]`分片
    - `x(...)`调用(函数,方法,类及其他可调用的)
    - `x.attr`属性引用
    - `(...)`元组,表达式,生成器表示法
    - `[...]`列表和列表解析
    - `{...}`字典,集合,字典和集合解析
  - 混合操作符的优先级
    - 操作符混合式,要依据其优先级进行运算
  - 括号分组的子表达式
    - 括号分组超越对象本身的优先级
  - 混合类型自动升级
    - python首先将被操作符操作的对象转换成其中复杂的操作对象,然后再对相同类型的操作对象进行数学运算
    - 整数 ==> 浮点数 ==> 复数: 依次更复杂
  - 运算符重载
    - 针对不同的操作对象,运算符代表不同的含义,也就是"多态"

- 变量和基本表达式

  - 变量
    - 变量在第一次赋值时被创建
    - 变量在表达式中使用时被替换为它们的值
    - 变量在表达式中使用以前必须已赋值
    - 变量像对象一样不需要在一开始进行声明

- 数字显示的格式

  - 交互模式的回显和打印的区别相当于内置`repr`和`str`函数

- 比较

  - 数值进行比较,返回布尔值

- 除法

  - `x/y`2.6之前此操作会省去小数部分;3.0后会保持小数部分
  - `x//y`floor除法,总会省略掉结果的小数部分,向下取整
  - 截断很重要,2.6和3.0的差别会影响很多

- 整数精度

- 复数

- 十六进制,八进制和二进制记数

- 位操作

  ```python
  >>> x = 1		# 二进制0001
  >>> x << 2		# 左移2位0100
  4
  >>> x | 2		# 二进制或(0001 | 0010)
  3
  >>> x & 1		# 二进制与(0001 & 0001)
  1
  ```

- 其他内置数学工具

  - 内置函数pow和abs
  - math模块

  ```python
  >>> import math
  >>> math.pi
  3.141592653589793
  >>> math.e
  2.718281828459045
  >>> pow(2,4)
  16
  >>> abs(-42.0)
  42.0
  >>> min(1,2,3)
  1
  ```

  - random模块

  ```python
  >>> import random
  >>> random.random()
  0.6680999893915853
  >>> random.randint(1,100)
  50
  >>> random.randint(1,100)
  25
  >>> random.choice(['john','mei','li'])
  'john'
  >>> random.choice(['john','mei','li'])
  'li'
  ```

- 其他数字类型

  - 核心: 整数, 浮点数, 复数

  - 小数数字

    - 浮点数缺乏精确度

    ```python
    >>> 0.1 + 0.1 + 0.1 - 0.3
    5.551115123125783e-17
    >>> print(0.1 + 0.1 + 0.1 - 0.3)
    5.55111512313e-17
    >>> from decimal import Decimal
    >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
    Decimal('0.0')
    ```

    - 设置全局精度

    ```python
    >>> import decimal
    >>> decimal.Decimal(1) / decimal.Decimal(7)
    Decimal('0.1428571428571428571428571429')
    # 设置四位数
    >>> decimal.getcontext().prec = 4
    >>> decimal.Decimal(1) / decimal.Decimal(7)
    Decimal('0.1429')
    # 设置两位数
    >>> decimal.getcontext().prec = 2
    >>> decimal.Decimal(1) / decimal.Decimal(7)
    Decimal('0.14')

    ```

    ​

    - 小数上下文管理器

    ```python
    >>> import decimal
    >>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
    Decimal('0.33')	# 以为上面例子设置了2位小数点精度
    >>> with decimal.localcontext() as ctx:
    ...     ctx.prec = 4
    ...     decimal.Decimal('1.00') / decimal.Decimal('3.00')
    ... 
    Decimal('0.3333')
    >>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
    Decimal('0.33')
    ```

    ​

  - 分数类型

    - ...

  - 集合

    - `set`这是一些唯一的,不可变的对象的一些无序集合,根据定义一个项只在集合中出现一次
    - 不可变限制和冻结集合
    - 由于不可重复性,可以用来将重复项从其他集合中过滤掉

    ```python
    >>> engineers = {'bob', 'sue', 'ann', 'vic'}
    >>> managers = {'tom', 'sue'}
    # 两个集合共有项
    >>> engineers & managers
    set(['sue'])
    # 两个集合所有项
    >>> engineers | managers
    set(['vic', 'sue', 'tom', 'bob', 'ann'])
    # 属于engineers不属于managers
    >>> engineers - managers
    set(['vic', 'bob', 'ann'])
    # 属于managers不属于engineers
    >>> managers - engineers
    set(['tom'])
    # managers 包含engineers
    >>> managers > engineers
    False
    # managers和engineers所有项包含engineers
    >>> (managers | engineers) > engineers
    True
    # managers和engineers中不相同的项
    >>> managers ^ engineers
    set(['vic', 'bob', 'ann', 'tom'])
    # managers和engineers中相同的项
    >>> (managers | engineers) - (managers ^ engineers)
    set(['sue'])
    ```

  - 布尔型

    - True
    - False

- 习题

  - 如何取得一个数字的平方根及平方

    ```python
    >>> import math
    >>> math.sqrt(9)	# 引入math模块,使用sqrt
    3.0
    >>> 3 ** 2
    9
    >>> pow(3,2)
    9
    ```

    ​

  - 如何能够截断或舍去浮点数的小数部分

    ```python
    # 引入math模块
    >>> import math
    >>> math.trunc(2.3)
    2
    >>> math.floor(2.32222)
    2.0
    # 内置函数round
    >>> round(2.3,0)
    2.0
    >>> round(2.32222,1)
    2.3
    >>> round(2.32222,3)
    2.322
    ```

    ​

  - 如何将一个整数转换为浮点数

    ```python
    >>> float(4)
    4.0
    # 或者python3.0之后的除法
    ```

    ​


  - 如何将一个整数显示成八进制,十六进制或二进制数

    ```python
    # 内置函数oct()和hex()
    >>> oct(10)
    '012'
    >>> hex(10)
    '0xa'
    ```

    ​

  - 如何将八进制,十六进制或二进制数转换成整数

    ```python
    # int(str, base)
    # 将一个字符串整数,按照2,8,16进制转为整数
    >>> int('012', 8)
    10
    >>> int('0xa', 16)
    10
    ```

    ​