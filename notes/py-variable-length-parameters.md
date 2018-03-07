# python可变参数

| 语法                  | 位置   | 解释                                                  |
| --------------------- | ------ | ----------------------------------------------------- |
| `def func(*name)` | 函数 | 匹配并收集(在元组中)所有包含位置的参数 |
| `def func(**name)` | 函数 | 匹配并收集(在字典中)所有包含位置的参数 |
| `def func(*args, name)` | 函数 | 参数必须在调用中按照关键字传递(python 3.x) |
| `def func(*, name=value)` | 函数 | 参数必须在调用中按照关键字传递(python 3.x) |
| `func(*sequence)` | 调用者 | 以name传递所有对象, 并作为独立的基于位置的参数        |
| `func(**dict)`    | 调用者 | 以name传递所有的关键字/值, 并作为独立的基于位置的参数 |

## 函数: 匹配并收集(在元组中)所有包含位置的参数

```python
>>> def func(*a):
...     print(a)
... 
>>> func(1,2,3,[1,2,3], {1:1,2:2,3:3})
(1, 2, 3, [1, 2, 3], {1: 1, 2: 2, 3: 3})
>>> def func(a,b,*c):
...     print(a)
...     print(b)
...     print(c)
... 
>>> func(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() missing 1 required positional argument: 'b'
>>> func(1,2)
1
2
()    # 没有传入参数, 生成空元组
>>> func(1,2,3,4,5,[1,2,3])
1
2
(3, 4, 5, [1, 2, 3])
```



##　函数: 匹配并收集(在字典中)所有包含位置的参数

```python
>>> def func(**a):
...     print(a)
... 
>>> func(a=1,b=2,c=3)
{'a': 1, 'b': 2, 'c': 3}
>>> func(a=1,b=2,c)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
# 传入参数时, 必须是以键值对的方式传入
>>> def func(a,b,**c):
...     print(a)
...     print(b)
...     print(c)
... 
>>> func(1,2,m=1,n=2)
1
2
{'m': 1, 'n': 2}
>>> func(1,2,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() takes 2 positional arguments but 3 were given
>>> def func(a,b,*c,**d):
...     """第三个参数及其后面的位置参数,都会收集到元组c中,关键字参数都会收集到字典d中"""
...     print(a)
...     print(b)
...     print(c)
...     print(d)
... 
# 有位置参数时, 关键字参数必须在位置参数后面
>>> func(1,2,3,4,5,x=1,y=2,6,z=3)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> func(1,2,3,4,5,x=1,y=2,z=3)
1
2
(3, 4, 5)
{'x': 1, 'y': 2, 'z': 3}
# 调用时, 可变参数可以为空
>>> func(1,2,x=1,y=2,z=3)
1
2
()
{'x': 1, 'y': 2, 'z': 3}
>>> func(1,2,3,4)
1
2
(3, 4)
{}
```

## 必须使用关键字参数的情况

```python
# "*"号之后的args变量名可以接受位置参数的元组, 之后必须使用关键字参数
def func(*args, name):
    ...
# "*"号之后必须使用关键字参数; 调用时参数只能给关键字参数
def func(*, name=value):
    ...
# 实例-1
>>> def func(*args, john=12, li):
...     print(john)
... 
>>> func(john=21)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() missing 1 required keyword-only argument: 'li'    # 必须有相应关键字参数
>>> func(john=21,li=22)
21
>>> func(1,2,john=21,li=22)
21
# 实例-2
>>> def func(*, john, li=12):
...     print(john)
...     print(li)
... 
>>> func(john=21)    # 在指定默认参数的情况下,可以不填相应关键字参数
21
12
>>> func(john=21, li=13)
21
13
```

## 解包: 以name传递所有对象, 并作为独立的基于位置的参数

```python
>>> def func(a,b,c,d):
...     print(a,b,c,d,sep='\n')
... 
>>> func(*"hell")
h
e
l
l
>>> func(*"hello")
# 调用需与函数定义参数数量对应, 否则触发参数异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() takes 4 positional arguments but 5 were given
>>> func(*"hel")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() missing 1 required positional argument: 'd'
```

## 解包: 以name传递所有的关键字/值, 并作为独立的基于位置的参数 

```python
>>> func(**{'a':1,'b':2,'c':3,'d':4})
1
2
3
4
>>> func(*(1,2),**{'c':3,'d':4})
1
2
3
4
```

