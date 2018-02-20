# 列表与字典

- 列表

  - 基本列表操作

  ```python
  >>> L = [1, 2, 3]
  >>> L2 = [4, 5, 6]
  >>> L + L2
  [1, 2, 3, 4, 5, 6]
  >>> L*3
  [1, 2, 3, 1, 2, 3, 1, 2, 3]
  >>> str(L) + '456'
  '[1, 2, 3]456'
  >>> L + list('456')
  [1, 2, 3, '4', '5', '6']

  ```

  ​

  - 列表迭代解析

  ```python
  >>> for x in L:
  ...     print(x, end='\n')
  ... 
  1
  2
  3
  >>> res = [c**2 for c in L]
  >>> res
  [1, 4, 9]
  >>> list(map(abs, [-1, -2, -3, 0, 1, 2, 3]))
  [1, 2, 3, 0, 1, 2, 3]
  ```

  ​

  - 索引,分片和矩阵

  ```python
  >>> L = [1, 2, 3]
  >>> L[1]
  2
  >>> L[-1]
  3
  >>> L[:]
  [1, 2, 3]
  >>> matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
  >>> matrix[1]
  [1, 2, 3]
  >>> matrix[1][1]
  2
  ```

  ​

  - 原处修改列表

  ```python
  >>> L = [1, 2, 3]
  >>> L[1] = -1	# 索引赋值
  >>> L
  [1, -1, 3]
  >>> L[:2] = [2, 1]	# 切片赋值
  >>> L
  [2, 1, 3]
  >>> L.append(4)	# append方法添加元素
  >>> L
  [2, 1, 3, 4]
  >>> L.append([5,6])	# 列表元素也可以是列表
  >>> L
  [2, 1, 3, 4, [5, 6]]
  >>> L.remove([5, 6])	# remove方法删除相应元素
  >>> L
  [1, 2, 3, 4]
  >>> L.sort()	# sort方法可对列表进行排序
  >>> L
  ['ABD', 'aBe', 'abc']
  >>> sorted(L, key=str.lower, reverse=True)	# sort方法可以使用参数
  ['aBe', 'ABD', 'abc']
  >>> L
  ['ABD', 'aBe', 'abc']
  >>> L.sort()
  >>> L
  ['ABD', 'aBe', 'abc']
  >>> sorted(L, key=str.lower, reverse=True)	# sorted方法不改变原列表顺序
  ['aBe', 'ABD', 'abc']
  >>> L
  ['ABD', 'aBe', 'abc']
  >>> L.extend(['abD'])	# 扩展元素
  >>> L
  ['ABD', 'aBe', 'abc', 'abD']
  >>> L.pop()	# 从后面开始剔除
  'abD'
  >>> L
  ['ABD', 'aBe', 'abc']
  >>> L.reverse()	# 列表相反排序
  >>> L
  ['abc', 'aBe', 'ABD']
  >>> list(reversed(L)) # 不改变原列表顺序
  ['ABD', 'aBe', 'abc']
  >>> L
  ['abc', 'aBe', 'ABD']
  # 堆栈,先进先出
  >>> L = [1, 2, 3]
  >>> L2 = []
  >>> L2.append(L.pop())
  >>> L2.append(L.pop())
  >>> L
  [1]
  >>> L2
  [3, 2]
  >>> L2.pop(0)
  3
  >>> L2
  [2]
  >>> del L2[:]
  >>> L2
  []
  ```

  ​

- 字典

  - 字典基本操作

  ```python
  # 创建字典
  >>> D = {'john':23,'li':22}
  >>> D
  {'john': 23, 'li': 22}
  # 常见字典常量和操作
  D = {}
  D = {'spam':2, 'eggs':3}
  D = {'food': {'ham':1,'eggs':2}}
  D = dict.fromkeys(['a','b'],0)
  D = dict(zip(keslist,valuelist))
  D = dict(name='Bob', age=42)
  D['eggs']
  D['food']['eggs']
  'eggs' in D
  D.keys()
  D.values()
  D.items()	# 键加值
  D.copy()	# 副本
  D.get(key,default)
  D.update(D2)	# 合并
  D.pop(key)	# 删除
  len(D)
  D[key] = 42
  del D [key]
  list(D.keys())
  D1.keys()&D2.keys()
  D = {x: x*2 for x in range(10)}	# 字典解析
  ```

  - 原处修改字典

  ```python
  >>> D = {'john':23,'li':22}
  >>> D['john'] = 25
  >>> D
  {'john': 25, 'li': 22}
  >>> del D['li']
  >>> D
  {'john': 25}
  ```

  ​

  - 字典的其他方法

  ```python
  >>> D = {'john':23,'li':22}
  >>> D2 = {'mei':21}
  >>> D.update(D2)
  >>> D
  {'john': 23, 'li': 22, 'mei': 21}
  >>> D.pop('mei')	# pop方法剔除一个键返回其值
  21
  ```

  ​

  - 语言表

  ```python
  >>> table = {'python': 'john',
  ...     'perl': 'li',
  ...     'js': 'mei'}
  >>> for lang in table:
  ...     print(lang, '\t', table[lang])
  ... 
  python 	 john
  perl 	 li
  js 	 mei
  ```

  ​

  - 字典注意事项

  - 为什么在意字典接口

    - 字典为信息存储提供了一种简洁的方法

  - 创建字典的其他方法

    - 赋值法

    ```python
    # 适合动态创建
    >>> dict = {}
    >>> dict['john'] = '23'
    >>> dict['li'] = '22'
    >>> dict
    {'john': '23', 'li': '22'}
    ```

    ​

    - 构造函数法

    ```python
    # 代码量较少,但键需是字符串;如果需要在程序运行时将键和值组成字典,此法比较合适
    >>> dict(john=23,li=22)
    {'john': 23, 'li': 22}
    >>> dict([('john',23),('li',22)])
    {'john': 23, 'li': 22}
    ```

    ​