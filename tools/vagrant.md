# vagrant简明手册

## 安装启动

```
$ git clone https://github.com/dongweiming/web_develop
# 克隆文件，文件中有vagrantfile设置文件
$ cd web_develop
# 进入目录
$ ssh-keygen
# 生成公钥
$ vagrant box add web_develop <virtualbox-location>
# 添加本地box
$ vagrant up
# 启动
$ vagrant provision 
# provision会执行vagrabtfile中的file命令，将本机的～/.ssh/id_rsa.pub复制到目标服务器，并保存为～/.ssh/authorized_keys.这会让系统自动登录
$ vagrant ssh
# 登录
```

---待续---
