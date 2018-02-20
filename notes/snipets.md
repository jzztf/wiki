- `if/else`三元表达式

```python
if a:
    b
else:
    c
#以上等效概括为
b if a else c
```



- lambda函数

```python
lambda argument1, argument2...argumentN: using arguments
```

- map函数

```python
map(function, iterable, ...)
# function: 函数, 有两个参数
# iterable: 一个或多个序列
# py 2.x返回列表;py 3.x返回迭代器
```

- 迭代器
  - 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
  - 迭代器是一个可以记住遍历的位置的对象。
  - 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
  - 迭代器有两个基本的方法：**iter()** 和 **next()**。
  - 字符串，列表或元组对象都可用于创建迭代器：
- 生成器
  - 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
  - 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
  - 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
  - 调用一个生成器函数，返回的是一个迭代器对象。

> 生成器的存在是为了在处理比较大的数据时, 能够减少内存消耗; 因为不用生成器, 我们可能生成一个列表, 在使用时, 不会是拿整个列表来使用, 而是会遍历使用; 那么在我们数据量很大时, 就没必要生成列表, 可以使用生成器, 在使用数据时, 一次只生成一个数据, 起到节省内存的作用.