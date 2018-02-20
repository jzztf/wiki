# python module time

## 获取当前时间

```python
>>> import time
>>> time.localtime(time.time())
time.struct_time(tm_year=2018, tm_mon=2, tm_mday=12, tm_hour=14, tm_min=37, tm_sec=24, tm_wday=0, tm_yday=43, tm_isdst=0)

```

## 获取格式化时间

```python
>>> time.asctime(time.localtime(time.time()))
'Mon Feb 12 14:42:52 2018'
```

## 格式化日期

```python
>>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
'2018-02-12 14:45:06'
>>> a = '2018-02-12 14:45:06'
>>> time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
1518417906.0
```

### python中日期符号

```python
%y	=>	两位数年份(00-99)
%Y	=>	四位数年份(000-9999)
%m	=>	月份(01-12)
%d	=>	月内某一天(0-31)
%H	=>	24时制(0-23)
%I	=>	12时制(0-12)
%M	=>	分钟数(00-59)
%S	=>	秒(00-59)
```
## 获取某月日历

```python
import calendar

print(calendar.month(2016,1))
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```
