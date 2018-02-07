## 域名: 

该仓库备份于github和coding两个位置, 域名分别为

- <https://jzztf.coding.me>
- <http://zhangtengfei.com>|<https://jzztf.github.io>

# 脚本操作

1. 推送：
   - 添加更新
   - 提交更新(包含提交信息)
   - push到远程仓库

```bash
$ ./post.sh "commit message"
```

2. 同步

```shell
$ ./sync.sh
```

## 结构

1. 原则: 大道至简

2. 结构示例

   - `index.md`包含整体结构所有文章链接,以二级标题和无序列表形式展示结构
   - "navigator.md"包含`index.md`中二级标题
   - 仓库目录向下不超三级

   ```shell
   # mdwiki
   $ tree
   ├── index.html							# mdwiki编译文件,将md文档转成html
   ├── index.md							# 首页,搜索页(Ctrl + f)
   ├── linux								# 二级目录(仓库目录算是一级)
   │   └── linux-update-sources-list.md
   ├── nav-linux.md						# nav导航文件
   ├── nav-others.md
   ├── nav-python.md
   ├── navigator.md						# 页面导航栏设置文件
   ├── others
   └── python								# 本着大道至简的原则,目录不超三级
       ├── py-basic						# 三级目录
       │   ├── py-funxtion.md
       │   ├── py-number.md
       │   └── py-string.md
       ├── py-pip.md
       └── py-virtualenv.md

   4 directories, 12 files
   ```



> 项目开始前, 先写README是有道理的!