# 迭代和解析

- 函数式编程?

  - map
  - filter
  - reduce

- 列表解析与map

  - 列表解析
    - 列表解析把任意一个表达式而不是一个函数应用到一个迭代对象中的元素

  ```python
  # 语法组成: 方括号, 表达式和一个序列组成
  >>> [2 ** x for x  in range(5)]
  [1, 2, 4, 8, 16]
  ```

  ​

  - map
    - map将列表中的元素应用到一个函数中
    - 可以是普通函数, 也可以是lambda函数

  ```python
  >>> list(map(lambda x: 2 ** x, range(5)))
  [1, 2, 4, 8, 16]
  >>> def func(x):
  ...     return 2 ** x
  ...
  # map(function_name, iter)
  >>> list(map(func, range(5)))
  [1, 2, 4, 8, 16]
  ```

  ​

- 增加测试和嵌套循环

  - 列表解析中添加if分支, 增加逻辑选择

  ```python
  >>> [x for x in range(5) if x % 2 == 0]
  [0, 2, 4]
  >>> list(filter((lambda x: x % 2 == 0), range(5)))
  [0, 2, 4]
  >>> [2 ** x for x in range(5) if x % 2 == 0]
  [1, 4, 16]
  # 为map函数添加一个filter选择
  >>> list(map((lambda x: 2 ** x), filter((lambda x: x % 2 == 0), range(5))))
  [1, 4, 16]
  # 列表解析的嵌套
  >>> [x + y for x in range(3) for y in range(5)]
  [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6]
  # 语法
  [expression for target_1 in iterable_1 [if condition_1]
  			for target_2 in iterable_2 [if condition_2]...]
  # 实例
  >>> [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
  [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

  ```

  ​

- 列表解析和矩阵

```python
>>> M = [[1,2,3],
...     [4,5,6],
...     [7,8,9]]
>>> M[1]
[4, 5, 6]
>>> M[1][1]
5
>>> M = [[1,2,3],
...     [4,5,6],
...     [7,8,9]]
>>> M[1]
[4, 5, 6]
>>> M[1][1]
5
# 取矩阵列数据
>>> [row[1] for row in M]
[2, 5, 8]
>>> [row[0] for row in M]
[1, 4, 7]
# 取对角线
>>> [M[i][i] for i in range(len(M))]
[1, 5, 9]
# 取乘积
>>> [M[row][col] * M[row][col] for row in range(3) for col in range(3)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]

```

- 理解列表解析

  - 从速度上看: 列表解析 > map > for

  ```python
  # 读取文件
  >>> [line.rstrip() for line in open('test.txt').readlines()]
  ['aaa', 'bbb', 'ccc']
  >>> [line.rstrip() for line in open('test.txt')]
  ['aaa', 'bbb', 'ccc']
  list(map(lambda line: line.rstrip(), open('test.txt')))
  ['aaa', 'bbb', 'ccc']
  ```

  ​


- 重访迭代器: 生成器

  - 生成器的存在在于避免占用过多内存, 在需要时进行迭代

    - 生成器函数: 编写常规def语句, 使用yield语句返回一次返回一个结果, 在每个结果之间挂起和继续它们的状态
    - 生成器表达式: 类似于列表解析, 但是它们按需返回生产结果的一个对象

  - 生成器函数yield vs return

    - 状态挂起: 与常规函数不同, 函数调用并不会结束, 而是挂起, 等待再一次调用, 知道除法可迭代对象的StopIteration异常
    - 迭代协议: 可迭代对象定义了一个`__next__`方法, 它要么返回迭代中的下一项, 或者引发一个StopIteration的异常来终止

  - 生成器函数应用

    ```python
    >>> def plus(N):
    ...     for i in range(N):
    ...             yield i + 1
    ... 
    >>> plus(5)
    <generator object plus at 0xb76ec86c>
    >>> next(x)	# 等同于x.__next__(): 
    1
    >>> next(x)
    2
    >>> next(x)
    3
    >>> next(x)
    4
    >>> next(x)
    5
    >>> next(x)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    # 也可以使用for循环, 迭代, 直至触发StopIteration异常
    >>> def plus(N):
    ...     for i in range(N):
    ...             yield i + 1
    ... 
    >>> x = plus(6)
    >>> for i in x: print(i, end=' : ')
    ... 
    1 : 2 : 3 : 4 : 5 : 6 : >>> 

    ```

  - send和throw

    - send(...)
       |      send(arg) -> send 'arg' into generator,
       |      return next yielded value or raise StopIteration.

    - throw(...)

       |      throw(typ[,val[,tb]]) -> raise exception in generator,
       |      return next yielded value or raise StopIteration.

    ```python
    # send可以传入生成器一个代码, 之后恢复之前的代码
    # ...

    ```

- 生成器表达式

  - 生成器表达式类似于列表解析, 只是使用圆括号

  ```python
  # 理解下列表表达式和生成器表达式
  >>> [x ** 2 for x in range(4)]
  [0, 1, 4, 9]
  >>> (x ** 2 for x in range(4))
  <generator object <genexpr> at 0xb76ec86c>
  >>> list(x ** 2 for x in range(4))
  [0, 1, 4, 9]
  # 生成器表达式
  >>> G = (x ** 2 for x in range(4))
  >>> next(G)
  0
  >>> G.__next__()
  1
  >>> next(G)
  4
  >>> G.__next__()
  9
  >>> next(G)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  # 不是每次调用就一定需要使用next
  # for循环遍历, 也会触发
  >>> for y in (x ** 2 for x in range(4)):
  ...     print(y)
  ... 
  0
  1
  4
  9
  # 如果生成器在其他函数括号内, 其本身的括号也不是必须的
  >>> sum(x ** 2 for x in range(4))
  14
  >>> sorted(x ** 2 for x in range(4))
  [0, 1, 4, 9]
  # 如果需要额外的参数, 则需要添加括号
  >>> sorted((x ** 2 for x in range(4)), reverse=True)
  [9, 4, 1, 0]
  ```

  ​

- 解析集合和字典解析

- 练习

  - 列表解析放在方括号和圆括号有什么区别
    - 列表解析表达式在方括号为"列表解析"
    - 列表解析表达式在圆括号中为"生成器"
  - 生成器和迭代器有什么关系
    - 生成器一次只返回一个数据, 是支持迭代协议的函数
    - 迭代器会将所有数据迭代返回
  - 如何辨别函数是否为生成器函数
    - 是否使用yield语句
  - yield语句是做什么的
    - 返回生成器对象, yield语句运行时会将函数状态挂起, 通过next函数调用, 直至触发"StopIteration"异常
  - map函数和list comprehension有什么关系,比较并对比
    - map函数将列表等可迭代对象中的元素分别作为参数传输给前置函数`map(func, iterable object)`
    - list comprehension是将可迭代对象传给表达式生成列表
    - 二者都比较底层, 运行速度要高于for循环和函数