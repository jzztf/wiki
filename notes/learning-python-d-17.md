# 作用域

- 全局变量名

  - 全局变量名是位于模块文件内部顶层的变量名
  - 全局变量如果是在函数内部被赋值的话, 必须经过声明
  - 全局变量名在函数内部不经过声明也可以被引用
  - 理解说明: 使用global语句全局化变量名前, 此变量名必须是在全局作用域中定义过的; 如果要对全局作用域的变量进行重新赋值并希望在全局作用域使用的话, 需要使用global语句声明; 如果只是在函数体内使用重新赋值的变量则不需要进行全局声明

- 作用域法则

  - 内嵌的模块是全局作用域
  - 全局作用域的范围仅限于单个文件
  - 每次对函数的调用都会创建一个新的本地作用域
  - 复制的变量名除非声明为全局变量或非本地变量,否则都为本地变量
  - 所有其他变量名都可以归纳为本地, 全局或内置

- 变量名解析

  - LEGB原则
    - Builtin(python)
    - 内置函数等, 可以直接使用
      - Global(module)
      - 全局变量是位于模块文件内部顶层的变量名
        - Enclosing function locals
          - Local(function)

- global语句  

- nonlocal语句

  - nonlocal语句是global语句的近亲

    - global语句用于def函数体中, 将本地变量声明为全局变量
    - nonlocal语句用于def函数体嵌套的函数体内, 将本地变量声明为上一层函数的变量

    ```python
    # global
    # global意味着名称位于一个嵌套的模块中
    >>> x = 5
    >>> y = 10
    >>> def global_test():
    ...     global x
    ...     x = 10
    ...     y = 20
    ... 
    >>> x, y
    (5, 10)
    >>> global_test()
    >>> x, y
    (10, 10)
    # nonlocal
    # nonlocal意味着名称位于一个嵌套的def函数体中
    ```


    ​```

- 工厂函数

  - 又叫闭合函数
  - 一个能够记住嵌套作用域的变量值的函数, 尽管那个函数不存在
  - 嵌套, 并返回

```python
>>> def factory_func():
...     def func():
...             x = 1
...             return x
...     return func()
... 
>>> factory_func()
1

```

- 其他访问全局变量的方法

```python
# thismod.py

var = 99

def glob():
    var = 0
    import thismod
    thismod.var += 1
    
def glob2():
    var = 0
    import sys
    glob = sys.modules['thismod']
    glob.var += 1
```

- 习题
  - 举出三四种python中保存状态信息的方法