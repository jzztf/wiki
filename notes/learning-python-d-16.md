# 函数基础

- 函数常见语句和表达式

```python
##Calls

myfunc("spam","eggs",meat=ham)
## def

def adder(a, b
## return

def adder(a, b=1, *c):
    return a+b+c[0]
## global

def changer():
    global x; x = 'new'
## nonlocal

def changer():
    nonlocal x; x = 'new'
## yield

def squares(x):
    for i in range(x): yield i ** 2
## lambda
Funcs = [lambda x: x**2, lambda x: x*3]
```

- 为什么使用函数

  - 最大化代码重用和最小化代码冗余
  - 流程分解

- 编写函数

  - def是可执行代码
  - def创建了一个对象并将其赋值给某一变量名
  - lambda创建一个对象但将其作为结果返回
  - return将一个结果对象发给调用者
  - yield向调用者发回一个结果对象,并记住它离开的地方
  - global声明一个模块级的变量并被赋值

- def

  - 语法
  - def语句创造了一个函数对象,并将其赋值给一个变量(函数名)

  ```python
  def <name> <arg1, arg2,...argN>:
  	...
      return value	# return语句为可选,如果没有则返回None
  ```

  - def语句是实时执行的, 它是一个可执行语句, 可以进行嵌套

  ```python
  if test:
      def func():
          ...
  else:
      def func():
          ...
  ...
  func()
  ```

  - 函数通过定义和调用实现功能

  ```python
  # 定义--defination
  >>> def add(a, b):
  ...    return a + b
  # 调用
  >>> add(2, 3)
  5
  ```

  - 多态

    - 对于操作符,能够体现python语言的多态
    - 函数亦能体现出python的多态

    ```python
    def intersect(seq1, seq2):
        res = []
        for x in seq1:
            if x in seq2:
                res.append(x)
         return res

    # intersect的参数只要是序列类型即可
    # 所以该函数可以操作多种类型,也是一种多态
    ```

    - 本地变量, return语句返回了res变量对应的对象, 其本身却消失了

- 练习

  - 编写函数意义
    - 避免代码冗余, 提高代码重用效率, 便于分割管理代码
  - 什么时候python将会创建函数
    - 当python运行到并执行def语句时,这个语句会创建一个函数对象并赋值给函数名
  - 当一个函数没有return语句时,它会返回什么
    - None
  - 在函数定义语句什么时候运行
    - 函数被调用时,主体就会被运行
  - 检查传入对象类型有什么错误
    - 检查传入对象的类型就是破坏函数的灵活性,将函数限制在固定的类型上; 没有类型检测, 函数可能处理所有可能的对象, 任何支持函数接口预期的对象都能用