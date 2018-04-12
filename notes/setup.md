# python中的setup文件

"setup.py"文件有两个作用,
- 一个是安装python包
- 二是创建自己的Python包
  - 标准的Python包包含以下三个文件
    - "setup.py" ==> 包的名称,版本,描述,作者信息,环境需求等参数
    - "setup.cfg" ==> 在包被创建时,会被setup.py读取
    - "MANIFEST.in" ==> 决定哪些东西要包含在python包中

实例:
来源: <https://pythonhosted.org/an_example_pypi_project/setuptools.html>
    
```python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_pypi_project",
    version = "0.0.4",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
```
