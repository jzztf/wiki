# 模块包

- 模块包
  - 包导入是把计算机上的目录变成另一个python命名空间, 而属性对应于目录所包含的子目录和模版
- 包导入基础

```python
# import 语句, 导入系统中位于dir1下的目录dir2中的mod模块
import dir1.dir2.mod

# from语句
from dir1.dir2.mod import x

# 点号表示目录的层级关系, 模块类似于属性
```



- 包和搜索路径设置
  - `__init__.py`
  - 如果选择使用包导入, 就必须多遵循一条约束, 包导入语句的路径中的每个目录内都必须有`__init__.py`这个文件
  - `__init__.py`文件, 就像普通模块一样, 也可以是空的, 但是为防止有相同名称的目录不小心隐藏在搜索路径中, 可以添加一些必要信息
  - `__ini__.py`文件扮演了"包"初始化的钩子, 替目录产生模块命名空间以及使用目录导入时实现from *行为的角色
- 包的初始化
  - python首次导入某个目录时, 会自动执行该目录下`__init__.py`文件中的所有程序代码, 因此这类文件自然成为放置包内文件所需初始化代码的场所, 比如: 创建所需要的数据文件, 连接数据库
  - 模块命名空间的初始化
  - `from *`: 作为高级功能, 可以在`__init__.py`文件内使用`__all__`列表来定义目录以`from *`语句形式导入时, 需要导出什么
    - 有待深入...
- 为什么要使用包导入
  - 在大程序中, 包让导入更具有信息性, 并可以作为组织工具, 简化末班的搜索路径, 而且可以解决模糊性
- 不使用包导入的局限

```python
/root
	/system1
    	utilities.py
    /system2
    	utilities.py
    /system3
    	main.py
# 如果位于system3中的main.py调用utilities,使用"import utilities" 
# 系统会在根目录下, 从左至右搜索, 充满不确定性
/root
	/system1
    	__init__.py
    	utilities.py
    /system2
    	__init__.py
    	utilities.py
    /system3
    	__init__.py
    	main.py
# 如果使用包导入, 添加"__init__.py"文件, 则在导入时使用路径
# "import system1.utilities"
# "import system2.utilities"
# 则明了很多
# "main.py"调用不需其本目录下有"__init__.py"文件, 但是以备被其他脚本调用, 可以提前添加该文件
```



- 相对导入

- 为什么使用相对导入

- 相对导入的作用域

- 为什么要在意模块包

  - 许多标准库都是按照包导入来访问的

  ```python
  from email.message import Message
  from tkinter.filedialog import askopenfilename
  from http.server import CGIHTTPRequest
  ```

  ​