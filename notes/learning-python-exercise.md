## 使用函数找出两列表的交集

```python
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
     return res
```

