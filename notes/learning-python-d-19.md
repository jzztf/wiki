# 函数的高级话题

- 递归函数

- 函数属性

- 注解

- lambda表达式

- map和filter函数式编程

- 函数聚合性和耦合性

  - 耦合性: 函数将如何通信
  - 聚合性: 如何将任务分解为更有针对性的函数
  - 特点
    - 耦合性: 对于输入使用参数并且对于输出使用return语句
    - 耦合性: 只有真正必要的情况下使用全局变量
    - 耦合性: 不要改变可变类型的参数, 除非调用者希望这样做
    - 聚合性: 每一个函数都应该有一个单一的, 统一的目标
    - 大小: 每一个函数都应该相对较小
    - 耦合性: 避免直接改变在另一个模块文件中的变量

- 匿名函数: lambda表达式

  - lambda表达式生成一个函数对象, 但是并返回; 而不是将函数对象赋值给一个变量名(函数名)
  - 语法: `lambda argument1,argument2,...argumentN : expression using arguments`
  - lambda是一个表达式,而不是一个语句
  - lamdba的主体是一个单个表达式, 而不是一个代码块

  ```python
  def func(x,y,z): return x + y + z
  # 等同于
  f = lamdba x, y, z: x + y + z

  ```

  - lamdba也能够使用默认参数

  ```python
  >>> f = (lambda a='fee', b='fie', c='foe': a + b +c)
  >>> f('wee')
  'weefiefoe'
  >>> f('wee', 'fi')
  ```

  - lambda好处

    - 达到一种函数速写的作用
    - 如果在lambda函数中实现`print`

    ```python
    import sys
    lambda x: sys.stdout.write(str(x)+'\n')
    ```

    ​

    - 如果在lambda函数实现循环

    ```python

    ```

    ​

- map函数

  - 语法: `map(func, args)`
  - map函数会对一个序列对象中的每一个元素应用到被传入的函数, 并且返回一个所有函数调用结果的列表

  ```(python
  >>> counters = [1,2,3,4]
  >>> def inc(x): return x + 10
  ... 
  >>> map(inc, counters)
  <map object at 0xb758360c>
  >>> list(map(inc, counters))
  [11, 12, 13, 14]
  # map函数也是lambda表达式出现次数较多的地方
  >>> list(map(lambda x: x + 10, counters))
  [11, 12, 13, 14]
  ```

  ​

- 函数式编程工具: filter和reduce

  - map函数是用来进行**函数式编程**的这类工具中最简单的内置函数代表
    - **函数式编程**就是对序列应用的一些函数的工具
  - filter函数: 基于某一测试函数过滤出一些元素

  ```python
  >>> list(range(-5,5))
  [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
  >>> list(filter((lambda x: x > 0), range(-5, 5)))
  [1, 2, 3, 4]
  # 序列中的元素返回值若为真的话会嵌入到列表中
  # 因为为内置函数,运行速度会高于其他
  >>> filter((lambda x: x > 0), range(-5, 5))
  <filter object at 0xb75dcc4c>

  ```

  ​

  - reduce函数: 对每个元素都应用函数并运行到最后结果

    - 2.6中为内置函数; 之后为functools模块中的一部分, 他接受一个迭代器来处理,但它本身不是一个迭代器

    ```python
    >>> from functools import reduce
    >>> reduce((lambda x, y: x + y), [1,2,3,4])
    10
    >>> reduce((lambda x, y: x * y), [1,2,3,4])
    24

    ```

    ​

  - filter和reduce函数都返回可迭代对象,可用list调用来显示其结果

- 递归函数

  - 直接或间接直接调用本身以进行循环的函数

```python
>>> def mysum(L):
...     if not L:
...             return 0
...     else:
...             return L[0] + mysum(L[1:])
... 
>>> mysum(range(100))
4950
>>> mysum(range(101))
5050

```

- 函数注解

  - 对于参数, 注解添加在参数后面的冒号之后
  - 对于返回值,注解添加在函数名之后`->`符号之后; 存储在键return之下

  ```python
  >>> def times(a: 'str', b: 'str') -> 'int': 
  ...     return a * b
  ... 
  >>> times.__annotations__
  {'a': 'str', 'b': 'str', 'return': 'int'}
  >>> def times(a: 'str'=4, b: 'str') -> 'int': 
  ...     return a * b
  ... 
  >>> times.__annotations__
  {'a': 'str', 'b': 'str', 'return': 'int'}
  # 添加注解的情况下添加默认值
  >>> def times(a: 'str'=4, b: 'str'=5) -> 'int': 
  ...     return a * b
  ... 
  >>> times()
  20
  >>> times.__annotations__
  {'a': 'str', 'b': 'str', 'return': 'int'}
  # 注解需要使用字符串表示
  ```

  ​


- 习题:
  - lambda表达式和def语句有什么关系
    - 共同点: 都会创建函数对象, 以便稍后调用
    - 不同点: lambda是表达式可以嵌入到函数定义def不发出现的地方, 比如其他表达式内部
    - lambda总是可以使用def来替代, 并通过变量名来引用函数
    - lambda只允许单个的返回值表达式, 因为它不支持语句代码块, 不适合较大的函数
  - 使用lambda的要点是什么
  - 比较和对比map,filter和reduce
    - 这3个内置函数都通过对一个序列(可迭代)对象以及集合结果中的各项应用另一个函数
    - map把每一项传递给函数并收集结果
    - filter收集那些函数返回一个True值的项
    - reduce通过一个累加器和后续项应用函数来计算一个单个的值(reduce在python3.0的functools模块中可用, 而不是在内置作用域中可用)
  - 什么是函数注解,如何使用
    - 函数注解在py3.0之后可用, 并且是函数的参数及其结果的语法上的修饰, 它会收集到分配给函数的`__annotations__`属性的一个字典中
  - 什么是递归函数,如何使用
    - 可以调用本身可以直接或间接地进行, 从而实现循环, 它可以遍历任意形状的结构, 也可以使用一般性迭代替代
  - 编写函数的通用设计规则是什么
    - 函数通常应该小, 尽可能自包含, 拥有单一的, 统一的用途, 并且与输入参数和返回值等其他部分通信; 如果期待修改的话, 他们可以使用可变的参数来与结果通信, 并且一些类型的程序暗含其他通信机制.