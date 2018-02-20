# while和for循环

- while循环

```python
while <test>:
    <statements>
else:
    <statements>
```

- break  ==> 跳出循环
- continue  ==> 调到最近循坏开头
- pass  ==> 空占位符
- else  ==> 只有在循坏离开时才会执行
- for循环

```python
for <target> in <object>:
    <statements>
else:
    <statements>
```

- 并行遍历

  - zip会将一个或多个序列为参数,返回元组列表

  ```python
  >>> L1 = [1, 2, 3, 4]
  >>> L2 = ['a', 'b', 'c', 'd']
  >>> zip(L1, L2)
  <zip object at 0xb6c0108c>
  >>> for i in zip(L1, L2):
  ...     print(i)
  ... 
  (1, 'a')
  (2, 'b')
  (3, 'c')
  (4, 'd')
  # 当两列表不一致时,zip会以最短的列表来截取
  ```

  ​

  - map会有zip类似的功能,但是在两列表不一致时,map会用None补齐缺少的元素
  - 使用zip构造字典

  ```python
  >>> keys = ['john', 'mei', 'li']
  >>> values = [23, 22, 21]
  >>> D2 = {}
  >>> for (k,v) in zip(keys, values):
  ...     D2[k] = v
  ... 
  >>> 
  >>> D2
  {'john': 23, 'mei': 22, 'li': 21}
  # 另一种
  >>> keys = ['john', 'mei', 'li']
  >>> values = [23, 22, 21]
  >>> D = {}
  >>> D = dict(zip(keys,values))
  >>> D
  {'john': 23, 'mei': 22, 'li': 21}

  ```

  - 产生偏移和元素

  ```python
  # 原始
  >>> offset = 0
  >>> for i in s:
  ...     print('s[' + str(offset) + ']' + "=" + "'" + i + "'")
  ...     offset += 1
  ... 
  s[0]='s'
  s[1]='p'
  s[2]='a'
  s[3]='m'
  # enumerate函数
  >>> for (offset, item) in enumerate(s):
  ...     print('s[' + str(offset) + ']' + "=" + "'" + item + "'")
  ... 
  s[0]='s'
  s[1]='p'
  s[2]='a'
  s[3]='m'
  # enumerate函数返回一个生成器对象,每次返回
  # enumerate函数有一个"__next__"方法,每次调用返回一个偏移值和元素的元组
  >>> E = enumerate(s)
  >>> next(E)
  (0, 's')
  >>> next(E)
  (1, 'p')
  >>> next(E)
  (2, 'a')
  >>> next(E)
  (3, 'm')

  ```

  ​

- 问答

  - while和for
    - while是一个通用的循环结构
    - for循环主要用来遍历序列类型对象的各项
  - break和continue
    - break会退出当前循环
    - continue会回到当前循环开头处
  - else分局何时执行
    - 再循环正常执行离开时执行一次
  - 如何编写一个计数器
    - 使用while循环手动生成
    - 使用for循环range函数生成
  - range函数
    - range函数可用于for循环执行固定次数的重复
    - 扫描实际元素,三重限制分片等可用其他方法替代