# 函数

## 基础

- def语句
- 定义和调用
- 多态

## 作用域

- 作用域基础
- global语句
- nonlocal语句

## 参数

- ​

## 函数的高级话题

- 递归函数
- 函数对象: 属性和注解
- 函数内省
- lambda函数
- 函数: map, filter和reduce

## 迭代和解析

- ​

## 练习

- 基础

  - 编写函数, 并将参数打印出来, 试着传递各种对象

  ```python
  >>> def echo(x):
  ...     print(x)
  ... 
  >>> echo("hello world!")
  hello world!
  >>> echo(123456)
  123456
  >>> echo([1,2,3,4,5])
  [1, 2, 3, 4, 5]
  >>> echo({"john": 23, "li": 22})
  {'john': 23, 'li': 22}
  >>> echo("hello", "world")
  # 传入两个参数时, 触发异常
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: echo() takes 1 positional argument but 2 were given
  ```

  ​


- 参数

```python
#!usr/bin/env python3

def adder(x,y):
	print(x + y)
	
adder("hello", "world")
adder([1,2,3],[5,6,7])
adder(1.22, 0.1)
```



- 可变参数
  - 计算任意数量的参数的和, 然后修改调用方式, 来传递两个以上或以下的参数; 返回值的和的类型是什么
- 关键字
  - ???
- 编写一个函数addDict(Dict1, Dict2), 接受两个字典参数, 返回时两个字典的并集, 如果传入的字典中有相同的键, 如果传入的是字典?

```python
def addDict(*dict):
	"""合并多个字典"""
	D = {}
	for d in dict:
		for k in d.keys():
			D[k] = d[k]
	print(D)
```



- 质数

```python
def get_prime(y):
	x = y // 2
	while x > 1:
		if y % x == 0:
			print(y, 'has factor', x)
			break
		x -= 1
	else:
		print(y, 'is prime')
```



- 列表解析

```python
import math

L = [x ** 2 for x in range(5)]
L_new = []

# 使用for循环
for x in L:
	L_new.apend(math.sqrt(x))
	
# 使用map调用
list(map(math.sqrt,L))

# 使用列表解析
[math.sqrt(x) for x in L]
```



- 计时工具
- ​