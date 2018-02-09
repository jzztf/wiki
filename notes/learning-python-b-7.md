## 字符串

- 字符串常量
- 单双引号字符串是一样的

```python
>>> 'hello' == "hello"
True
```



- 用转义序列代表特殊字节
  - `\n`换行符
  - `\t`制表符
  - `\`忽视(连续)
  - `\'`单引号
  - `\"`双引号
  - `\a`响铃
  - `\b`倒退
  - `\f`换页
  - `\r`返回
  - `\v`垂直制表符
  - 等等
- raw字符串抑制转义

```python
>>> print(r"hello\n world")
hello\n world
>>> print("hello\n world")
hello
 world
```



- 三重引号编写多行字符串
  - 多行字符串
  - 多行注释


- 实际应用中的字符串

  - 基本操作

  - 索引和切片

    - 扩展str[I:J:K]
    - 切片每隔K个元素, 从I-J进行切片

    ```python
    >>> str = "abcdefg"
    >>> str[::-1]
    'gfedcba'
    >>> str[1:5]
    'bcde'
    # 复数对边界进行了反转
    >>> str[5:1:-1]
    'fedc'
    ```

    ​

  - 为什么要在意: 切片

    - 切片有很多应用场景,比如程序参数检测

  - 字符串转换工具

    - `str()`
    - `ord()`会将字符串转换为其对应的ASCII码
    - `chr()`会与上面函数执行相反的结果

  - 修改字符串

    - 字符串不可变性质,不能在原地进行修改,比如索引赋值就会引发错误

    ```python
    >>> str = 'hello world'
    >>> str[0] = 'H'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    ```

    ​

  - 字符串方法

    ```python
    >>> s = "hello world"
    >>> dir(s)
    ```

    ​

  - 字符串方法实例: 修改字符串

  - 字符串方法实例: 文本解析

  - 实际应用中的常见字符串方法

  - 字符串格式化表达式

  - 字符串格式化调用方法

    - 基础知识
    - 添加键, 属性和偏移量
    - 添加具体格式
    - 与%格式化表达式比较
    - 为什么用新的格式化方法
    - 同样分类的类型共享其操作集合
    - 可变类型能够在远处修改