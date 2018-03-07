# 高级模块话题

- 数据隐藏

  - python模块会导出其文件所赋值的所有变量名, 没有对某一变量名声明, 使其在模块中可见或不可见的概念. 只要客户想修改, 也是可有办法修改的.

  - python中模块的数据隐藏是一种惯例, 而不是一种约束

  - 方式

    - 最小化`from *`的破坏, 使用`_X`和`__all__`

    ```python
    # 在模块顶层把变量名的字符串列表赋值给变量"__all__"
    # 在"__init__.py"中设置, 在使用"import *"导入时, 只会显示出列表中列举的内容
    __all__ = ["Error", "encode", "decode"]
    # "_X"的作用刚好相反, 目的在于不被复制的变量名
    # 在需要复制变量名时, python会先搜索"__all__"列表; 如果没有定义"__all__"的话, 再搜索没有以下划线"_"开头的变量名
    ```

    ​

- `__future__`模块

- `__name__`变量

  - 如果文件是作为主程序被运行, 则其`__name__`属性为字符串`__main__`; 如果被当做模块运行, 则属性`__name__`为其本身当做模块的名称
  - **用途**: 可以给每个脚本程序添加`__name__`属性, 进行输出测试, 而其本身其他代码可用来导入. 

```python
# 测试文件
#!/usr/bin/env python3

"""测试__name__ == '__main__'"""

def tester():
	print("this is main")
	
if __name__ == '__main__':
	tester()
# shell
$ python3 test_name.py
this is main
$ python3
# python3
>>> import test_name
>>> test_name.__name__
'test_name'

```



- 修改模块搜索路径

  - 修改模块搜索路径是对环境变量"PYTHONPATH"以及可能的".pth"进行修改
  - sys.path修改

  ```python
  >>> import sys
  >>> sys.path
  ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
  # 添加环境变量, 模块搜索路径
  >>> sys.path.append('~/tmp')
  >>> sys.path
  ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages', '~/tmp']
  # 剔除最后添加的
  # 同时sys.path具备remove(value)方法; 具体可查看help(sys.path)
  >>> sys.path.pop()
  '~/tmp'
  >>> sys.path
  ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
  ```

- import语句和from语句的as扩展

  - import语句和from语句均为对引入模块和方法或属性进行重新赋值
  - 在包导入使用中, 前缀太长可使用import...as...语句, 进行重命名


- 模块是对象: 元程序

  - 因为模块通过内置属性显示了它们的大多数有趣的特性, 因此, 可很容易地编写程序来管理其他程序, 这类管理程序被称为"元程序"(metaprogram或内省-introspection), 也就是用来处理程序的程序被称作"元程序"

- 列表工具

- 通过名称字符串来运行模块

  - 以一个字符串的形势获取要导入的模块的名称
  - 直接使用"import"语句导入字符串会引发错误, 可使用`exec`语句

  ```python
  modname = "string-module"
  exec("import " + modname)  # "import "需要在"import"之后加一空格
  # "exec"命令实际执行字符串"import module"
  # 缺点: 每次执行"exec"命令都会编译import语句
  # 如果需要导入多次, 可以直接使用内置的"__import__"函数来导入字符串
  modname = "string-module"
  string = __import__(modname)  # 将模块名赋值给变量string
  ```

- 过渡式重载

  - 模块在重载时, 不会使更深层次的模块重载
  - 比如: 程序A导入模块B, 模块B导入了模块C, 当模块B发生了变化, 在模块A中进行了重载, 则该重载也只是重载了模块B, 而不会延伸重载模块C
  - 在大程序中, 如果手动重载, 工作量会很大, 这时可以在每个模块添加reload调用, 完成所有模块的重载

  ```python
  # reloadall.py


  ```

  ​

- 模块的设计理念

  - 总是在你python模块内编写代码
  - 模块耦合度要降到最低: 全局变量
    - 模块如果类似于函数的闭合, 模块会运行的很好
  - 最大化模块黏合性: 统一目标
    - 模块的所有元素都享有共同的目标, 如此不太会依赖外部变量
  - 模块应该少去修改其他模块的变量


- from复制语句, 而不是连接

  - from语句只是将两个变量名复制, 而不是连接, 修改变量名, 不会引起模块变量的变化

- from*语句在文件中最多使用一次, 使用多个时会造成语义错乱

- reload语句不会影响from导入

  - 为保证重载有效, 可以使用import以及点号运算, 因为点号运算总是回到模块

  ```python
  from module import x
  ...
  from imp import reload
  reload(module)
  x						# x依然旧对象
  =====================================
  import module
  ...
  from imp import reload
  reload(module)
  module.x				# x已重载为新对象
  ```



- reload, from以及交互模式测试

  - 使用from语句导入某个方法时, 重载后, 某方法为复制的原模块中的变量, 并不会更新, 如果需要重新使用, 需要重新调用from语句

  ```python
  from module import x
  ...
  from imp import reload
  reload(module)
  from module import x	# 重载模块后, 需要重新载入
  ```

- 互相导入的模块被称为"递归导入"

  - 小心设计, 尽量不要互相导入模块, 因为语句是一条条运行的, 在有时需要时, 可能某变量还不存在

- 使用`__future__`导入新特性

- 练习:

  - 模块顶层以下划线开头的变量名的重要性

    - 模块顶层变量名以单个下划线开头时, 在使用`from *`语句时不会被导入, 但是可以通过`import`和普通`from`语句导入

  - 模块的`__name__`是字符串`"__main__"`时, 代表了什么意义

    - `__name__=="__main__"`表示该脚本在被当做主程序运行, 在被当做模块被导入时, `__name__`为其本身模块名

  - 如果用户通过交互模式输入模块的变量名进行测试, 应该怎么导入?

    - 此时交互模式下输入的模块名会被当做字符串处理, 所以要处理以字符串导入模块, 使用`exec`语句

    ```python
    module = "module"
    exec("import " + module)  # import字符串内要留一空格
    -----------------------------------------
    如果要导入多次, 可使用模块本身的"__import__"方法
    module = "module"
    module = __import__(module)
    ```

    ​

  - 改变`sys.path`和设置PYTHONPATH来修改模块搜索路径有什么不同?

    - sys.path修改的模块搜索路径是暂时的, 只能作用于正在运行的脚本; 设置PYTHONPATH是永久的
    - python搜索的四个路径为
      - 程序主目录
      - PYTHONPATH目录
        - python会从左至右搜索该列表中列举的所有目录
      - 标准链接库目录
      - 任何`.pth文件的内容`
        - 放在合适的目录中, 比如主程序目录


  - ​