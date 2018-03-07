# "%"格式化

## 基础

```python
>>> print('hello %s, welcome to my website!'%('john'))
hello john, welcome to my website!
# 支持多个字符串格式化, 只需提供字符串元组
>>> print('hello %s, welcome to my %s!'%('john','blog'))
hello john, welcome to my blog!
```
## 高级

- 常见字符串格式化代码

```python
s    =>    字符串
d    =>    十进制(整数)
i    =>    整数
o    =>    八进制(整数)
x    =>    十六进制(整数)
X    =>    十六进制(整数, 大写)
e    =>    浮点指数
E    =>    浮点指数(大写)
f    =>    浮点十进制
F    =>    浮点十进制
g    =>    浮点e或f
G    =>    浮点E或F
%    =>    常量
```

- 高级语法

  ```python
  %[(name)][flags][width][.precision]typecode
  ```

  - (name)为字典的键key, 格式化后显示相应值value

  ```python
  >>> print('li: %(li)s'%{'li': 89, 'mei': 78})
  li: 89
  ```

    - [flags]为"-"左对齐, "+"正负号, "0"补零标志位

  ```python
  >>> print('%-5s:\n%-5s:'%('name', 'age'))
     e :
       :
  >>> print('%+d'%(123))
  +123
  >>> print('%06d'%(123))
  000123
  ```

    - [width]为格式化后字符串所占位数, 也可以理解为选择一个宽度, 进行右对齐

  ```python
  >>> print('%-5s:%5s\n%-5s:%5d'%('name','john', 'age', 23))
  name : john
  age     :   23
  ```

    - [.precision]为格式化字符串的精确度, 注意要加点号

  ```python
  >>> print('%.3f'%(1/3))
  0.333
  >>> print('%.4f'%(1/3))
  0.3333
  ```

    - 宽度和精确度, 都可以使用"\*"号, 在后期添加, 注意精确度使用的时".\*", 不要忘记点号

  ```python
  >>> print('%-5s:%*s\n%-5s:%*d'%('name', 5,'john', 'age', 5, 23))
     e : john
       :   23
  >>> print('%.*f'%(4,1/3))
  0.3333
  ```

    - typecode就是常见字符串格式化代码, 比如"s"为字符串, "d"为十进制整数, "f"为浮点数