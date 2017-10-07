# pip简明手册

> pip是Python包管理工具

## pip安装

> **[pip install](https://pip.pypa.io/en/stable/installing/)**

- 下载`get-pip.py`
- 执行`python get-pip.py`
- 使用参数`--no-setuptools`&`--no-wheel`,只安装pip不安装"setuptool"和"wheel"

## pip的基本使用

- 更新`pip install -U pip`
- 安装包`pip install packages`,安装指定版本`pip install packages==1.o.4`
- 列出包`pip list`,列出过期包`pip list --outdated`,展示包信息`pip show packages`

## 生成和安装requirements.txt

```bash
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

## 从国内镜像安装

> **[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/)**

```bash
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
```
## 修改安装源

Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件)

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host=mirrors.aliyun.com
```
