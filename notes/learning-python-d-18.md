# 参数

- 传递参数
  - 参数传递是通过自动将对象赋值给本地变量名来实现的
  - 在函数内部的参数名的赋值不会影响调用者
  - 改变函数的可变参数的值也许会对调用者有影响
    - 因为参数是简单地赋值给传入的对象,函数能够就地改变传入的可变对象, 因此其结果会影响调用者
    - 不可变参数"通过值"进行传递
    - 可变对象是通过"指针"进行传递
    - 如果希望避免可变对象被函数修改可以复制可变对象进行操作
- 特定的参数匹配模型
  - 位置参数: 从左至右进行匹配
  - 关键字参数: 通过参数名进行匹配
  - 默认参数: 为没有传入值的参数定义参数值
  - 可变参数: 收集任意多个基于位置或关键字的参数, 使用`*`号表示多个元素
  - 可变参数解包: 传递人一多的就有位置或关键字的参数
    - 函数头部的`*`号意味着收集更多的参数, 而在调用者中表示传递任意多的参数 
  - keyword-only参数: 参数必须按照名称来传递
- 匹配语法

```python
func(value)					=> 调用者 => 常规参数: 通过位置进行匹配
func(name=value)			=> 调用者 => 关键字参数: 通过变量名匹配
func(*sequence)				=> 调用者 => 以name传递所有的对象, 并作为独立的基于未知的参数
func(**dict)				=> 调用者 => 以name成对的传递所有关键字/值, 并作为独立的关键字参数
def func(name)				=> 函数 => 常规参数: 通过位置或变量名进行匹配
def func(name = value)		=> 函数 => 默认参数值, 如果没有在调用中传递的话
def func(*name)				=> 函数 => 匹配并收集(在元组中)所有包含位置的参数
def func(**name)			=> 函数 => 匹配并收集(在字典中)所有包含位置的参数
def func(*args, name)		=> 函数 => 参数在调用中必须使用关键字传递
def func(*, name=value)		=> 同上python3
```

- 任意参数

  - 在元组中收集不匹配位置参数

  ```python
  >>> def func(*args):
  ...     print(args)
  ... 
  >>> func()
  ()
  >>> func(1)
  (1,)
  >>> func(1,2,3,4)
  (1, 2, 3, 4)
  ```

  - 在字典中收集不匹配位置参数

  ```python
  >>> def f(**args):
  ...     print(args)
  ... 
  >>> f()
  {}
  >>> f(a=3, b =4)
  {'a': 3, 'b': 4}
  >>> f(a=3, b=4, c=5, d=6, e=7)
  {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7}
  ```

  ​

- 解包参数

  - 解包元组

  ```python
  >>> def func(a,b,c,d):
  ...     print(a,b,c,d)
  ... 
  >>> t = (1,2,3,4)
  >>> func(*t)
  1 2 3 4
  >>> for i in func(*t):
  ...     print(i)
  ... 
  1 2 3 4
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'NoneType' object is not iterable
  # func(*t)只会返回一个None类型
  ```

  - 灵活解包(基于关键字参数)

  ```python
  >>> func(*(1,2),**{'d':4,'c':3})
  1 2 3 4
  >>> func(1, *(2,3),**{'d':4})
  1 2 3 4
  >>> func(1,c=3,*(2,),**{'d':4})
  1 2 3 4
  # 在不能预测传入参数的数量时此方法比较有用
  ```

  ​

- keyword-only参数

  - 参数列表使用一个`*`号, 表示函数不会接受一个变量长度的参数列表, 期待跟在*后面的参数都作为关键字传递

```python
>>> def kwonly(a, *b, c):
...     print(a,b,c)
... 
>>> kwonly(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwonly() missing 1 required keyword-only argument: 'c'
>>> kwonly(1,2,c=3)
1 (2,) 3
>>> kwonly(1,2,3,4,5,c=3)
1 (2, 3, 4, 5) 3

```

