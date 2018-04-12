
Flask-MySQLdb 为Flask提供 MySQL 连接

# 安装

`pip install flask-mysqldb`

# 使用实例

```python
from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL(APP)

# set MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ztf'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

"""
在默认情况下cursor方法返回的是BaseCursor类型对象，
BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。
如果要返回字典(dict)表示的记录，
就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。
"""



@app.route('/register')
def register():
	
	# create cursor
	cur = mysql.connection.cursor()
	
	# execute query
	cur.excute("mysql command")

	# commit
	mysql.connection.commit()

	# close connection
	cur.close()

