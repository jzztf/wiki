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

  ```python
  >>> list(map(lambda x: 2 ** x, range(5)))
  [1, 2, 4, 8, 16]

  ```

  ​

- 列表解析和矩阵

- 重访迭代器: 生成器

  - 生成器函数yield vs return

- 解析集合和字典解析