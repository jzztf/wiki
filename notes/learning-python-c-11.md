# 赋值表达式和打印

- 赋值语句
  - 赋值语句建立对象引用值
  - 变量名在首次赋值时会被创建
  - 变量名在引用前必须先赋值
  - 执行隐式赋值的操作: 模块引入
- 赋值语句的形式

```python
spam = 'spam'					=> 基本形式
spam, ham = 'yum', 'YUM'		=> 元组赋值运算
[spam, ham] = ['yum', 'YUM']	=> 列表赋值运算
a, b, c, d = 'spam'				=> 序列赋值运算
a, *b = 'spam'					=> 扩展序列解包; 用字符串的第一个字母匹配a,剩下的匹配b
spam = ham = 'lunch'			=> 多目标赋值运算
spams += 42						=> 增强赋值运算
```

- 表达式语句

```python
spam(eggs,ham)
spam.ham(eggs)
spam
print(a,b,b sep='')
yield x ** 2
```

- 打印操作

```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
sep	=> 每个对象之间添加
end	=> 对象结尾添加
file => 系统标准输出
# 重点 ==>
import sys
sys.stdout = open('log.txt', 'a')
...
print(x,y,z)	# 程序中的任何语句都会打印到log.txt中
sys.stdout.close()

# 3.0特性重设
log = open('log.txt', 'a')
print(x, y, z, file=log)
print(a, b, c)
```

