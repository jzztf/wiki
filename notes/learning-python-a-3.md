# 一 使用入门

## 1. 问答

## 2. python如何运行程序

- python解释器: python是一个名为解释器的的软件包,解释器是一种让其他程序运行起来的程序,当编写了一段程序,python解释器将读取程序,并按照指令执行得到结果
- 源代码(m.py) ==> 字节码编译(m.pyc) ==> python虚拟机(PVM)
- 目前所使用的都是Cpython,底层通过C语言实现;底层通过java实现的叫做Jpython
- 冻结二进制(frozen binary),可以使得代码直接运行(Windows使用"py2exe";linux使用"PyInstaller")

## 3. 如何运行程序

- 交互模式下编写代码

  - linux => shell中输入`python`或者`/usr/local/bin/python`
  - windows => shell窗口输入`python`或者开始菜单点击`IDLE`

  ```shell
  # linux
  ~ python
  Python 2.7.13 (default, Nov 23 2017, 15:37:09) 
  [GCC 6.3.0 20170406] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> print("hello world")
  hello world
  >>> 2 ** 3
  8
  >>> a = 3
  >>> a
  3
  ```

  - 交互模式不会将代码写入文件,会根据用户输入直接反馈结果
  - 交互模式是体验语言和测试程序的好地方
    - 交互模式只能输入python命令
    - 文件中打印语句是必须的,交互模式下会直接返回结果
    - 交互模式不需要缩进,必要时其会自动缩进
    - 使用复合语句时提示符会变成三个点`...`而不再是`>>>`
    - 交互模式下空行结束复合语句,也就是复合语句完成后两个`Enter`键就可以了
    - 交互模式一次只能运行一个语句

- 系统命令行和文件

  - 编写一个python脚本在命令行中运行并重定向输出到文件

  ```python
  #!/usr/bin/env python
  # get_platform_info.py
  import sys
  print(sys.platform)
  ```

  ```shell
  $ python get_platform_info.py > platform_info.md
  ```

  - windows上如果不指定后缀名,会自动生成txt.

  - python文件在作为模块被导入时不需扩展名;在作为脚本程序被运行时需要扩展名: `$ python test.py`

  - 文件中获取信息需要使用print语句

  - linux注意事项

    - `shabang` => `#!`,linux中识别脚本文件的开头

    - linux下编写python文件,可在开头写`#!/usr/local/bin/python`

    - 或者使用linux的查找功能`#!/usr/bin/env python`

    - linux下执行python脚本`$ python test.py`

    - 也可以直接赋予其权限

      ```shell
      $ chmod 755 test.py
      $ ./test.py
      ```

      ​

- 点击文件图标

  - windows下可以通过点击图标运行程序
  - 但是程序会一闪而过,可以使用`input()`产生一个等待输入的窗口好展示结果
  - 也可以添加一些信息`input("Enter 'exit()' to exit")`
  - 另一个问题是如果脚本出现问题,也不会得到反馈,因为窗口一闪而过,后面使用异常可以捕获一些错误

- 模块的导入和重载

  - 默认情况下,模块只在一次会话中引入一次
  - 也就是当修改了模块文件并保存了,但是交互模式下是在之前引入的,后面的修改就会得不到显示,此为有意设计,因为导入操作开销很大,避免重复导入,耗费资源
  - 如果要更新导入模块,可以引入`imp`标准库模块

  ```python
  >>> from imp import reload
  >>> reload(test_model)
  ```

  - 模块的先要特性: 属性

    - 模块是变量名的封装,通过点号可以调用模块的变量也就是属性
    - from语句相比于import对模块进行了重命名

    ```python
    >>> import imp
    >>> imp.reload(test_model)
    # ==> 等同于
    >>> from imp import reload
    >>> reload(test_model)
    ```

    - 当同时引入多个变量时,调用多个变量的值时其会以元组的形势出现

    ```python
    # test.py
    # a = 'john'
    # b = 'li'
    # c = 'mei'

    >>> from test import a, b, c
    >>> b, c
    ('li', 'mei')
    ```

  - 模块和命名空间

    - python程序往往由多个模块文件构成,每个模块都构成了独立命名空间,在直接调用时使用点号调用,避免冲突
    - 争议: 使用from语句相比import更可能引起变量名冲突或覆盖,不过自己的变量名自己掌控出现问题的可能性不大

  - import和reload

    - 重载模块只会重载定义的模块,而不会重载该模块中导入的模块,如果变更了多个模块,那么就需要注意了!
    - 最好将多有需要导入的模块放在一个工作目录中

- 使用exec运行模块文件

  - 使用`exec(open('module.py').read())`无需在模块修改后再次重载
  - 但是也会存在一个问题:在调用属性时如果其和变量名一样,之前的变量名会被覆盖

- IDLE用户界面

  - ...

- 其他IDE

  - ...

- 其他启动选项

  - ...