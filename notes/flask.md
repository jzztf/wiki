# flask 快速入门

## 最小测试应用

```python
#coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Index"

if __name__ == '__main__':
	app.run(debug=True)

# http://127.0.0.1:5000/可访问
# 增加外部访问
# app.run(host='0.0.0.0')
# 调试模式
# app.run(debug=True)
#!!! 交互模式不可使用在生产环境
```

##  路由

route装饰器会将函数绑定到对应的url上,url会触发函数

```python
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World'
# '/'根目录url会触发函数index(),返回"Index Page"
# '/hello'url会触发函数hello(),返回"Hello World"
```

### 动态URL

添加特殊字段标记,使用动态URL

```python
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@ppp.route('post/<int:post_id')
def show_post(post_id):
	return 'Post %d' % post_id
# 特殊标记"<变量名>",会和函数中"变量名"标记一致
# 转换器标记"<转换器:变量名>"
# 转换器:"int"接受整数;"float"接受浮点数;"path"和默认相似,但也接受斜线
```

### 唯一的URL和重定向行为

```python
@app.route('/projects/')
def projects():
	return 'The projects page'

@app.route('/about')
def about():
	return 'The about page'

# 规范URL带斜线,即使用户输入不带斜线的URL也会被定向到带斜线的URL
# 不带斜线的URL,如果用户在URL中,添加了斜线,则会引发错误
# 如此规定,既保证URL的唯一性,也不会使得搜索引擎搜索两次

```

