# virtualenv

## virtualenv快速使用

```
$ virtualenv --no-site-packages venv    # 设置   
$ source ./env/bin/activate       # 激活 
(venv)$ deactivate         # 关闭
```
## 参数"--no-site-packages"

> 默认情况下，虚拟环境会依赖系统环境中的site packages，就是说系统中已经安装好的第三方package也会安装在虚拟环境中，如果不想依赖这些package，那么可以加上参数`--no-site-packages`建立虚拟环境

## 一般安装使用

```
$ virtualenv .venv      # virtualenv + 虚拟环境名称
```
## 指定Python版本

```
$ virtualenv .venv --python=python3
```
