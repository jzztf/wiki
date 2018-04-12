# howto sorting in python

## 内置函数"sorted()"和方法".sort()"

- "sorted()"和".sort()"都可对列表对象进行排序;


```python
>>> sorted([5,2,3,1,4])
[1, 2, 3, 4, 5]

>>> a = [5,2,3,1,4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
```

- "sorted()"可对任何可迭代对象排序

```python
>>> sorted({1:'d',2:'b',3:'e',4:'f',5:'a'})
[1, 2, 3, 4, 5]

>>> d = {1:'d',2:'b',3:'e',4:'f',5:'a'}
>>> D = {}
>>> for k in sorted(d):
...     D[k] = d[k]
... 
>>> D
{1: 'd', 2: 'b', 3: 'e', 4: 'f', 5: 'a'}
```

## key函数

- ".sort()"和"sorted()"都有一个key参数,定义一个函数,依照此函数进行排序

```python
>>> sorted("This is a test string from Andrew".split(),key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

>>> students_tuples = [
...     ('john','A',15),
...     ('jane','B',12),
...     ('dave','B',10)
]
>>> sorted(students_tuples,key=lambda student: student[2])
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> class Student:
...     def __init__(self,name,grade,age):
...             self.name = name
...             self.grade = grade
...             self.age = age
...     def __repr__(self):
...             return repr((self.name,self.grade,self.age))
... 

>>> class Student:
...     def __init__(self,name,grade,age):
...             self.name = name
...             self.grade = grade
...             self.age = age
...     def __repr__(self):
...             return repr((self.name,self.grade,self.age))
... 

>>> students = [
...     Student('john','A',15),
...     Student('jane','B',12),
...     Student('dave','B',10)
        ]

>>> sorted(students,key=lambda student: student.age)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(students,key=lambda student: student.grade)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

## operator模块中"itemgetter"和"attrgetter"

```python
>>> from operator import itemgetter,attrgetter
>>> sorted(students_tuples,key=itemgetter(1))
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(students_tuples,key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(students,key=attrgetter('grade'))
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

```

## 升序和降序

```python
>>> sorted(students,key=attrgetter('age'),reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

## 排序稳定性和复杂排序

当排序对象有相同项时,会按照原始顺序进行排序

```python
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data,key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
>>> sorted(data,key=itemgetter(1))
[('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
```
