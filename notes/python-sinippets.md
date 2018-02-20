## 为字典排序

```python
# 方法1
D = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
keys = list(D.keys())
keys.sort()
for key in keys:
    print(key + " => " + str(D[key]))
a => 1
b => 2
c => 3
d => 4
e => 5
f => 6
g => 7
# 方法2
for key in sorted(D):
    print(key + " ==> " + str(D[key]))
a ==> 1
b ==> 2
c ==> 3
d ==> 4
e ==> 5
f ==> 6
g ==> 7
```

