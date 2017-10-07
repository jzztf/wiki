# Ruby Basic

## 安装rvm

ruby版本管理器

- [rvm官网](https://www.rvm.io/)
- [install说明](https://www.rvm.io/rvm/install)

```bash
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
$ \curl -sSL https://get.rvm.io | bash -s stable
$ source ~/.bashrc
$ source ~/.bash_profile
```

## 修改国内镜像源

- [安装指引](https://ruby-china.org/wiki/rvm-guide)(ruby-china)

```bash
$ echo "ruby_url=https://cache.ruby-china.org/pub/ruby" > ~/.rvm/user/db
$ gem sources -l
*** CURRENT SOURCES ***

https://gems.ruby-china.org/
```

## 安装ruby

```bash
$ rvm list known # 列出已知ruby版本
$ rvm install 2.4.1 --disable-binary # 安装最新版本
$ rvm use 2.4.1 # 切换ruby版本
$ rvm user 2.4.1 --default # 默认ruby版本
$ rvm list # 查询已经安装的ruby
$ rvm remove 2.2.0 # 移除2.2.0版本
```

## gem

> gem(RubyGems)是一个用于对ruby组件进行打包的ruby打包系统，类似于linux中的`apt-get`, python中的`pip`.安装完ruby，就已经安装了gem

## gemset

gemset类似于python的virtualenv

```bash
$ rvm use 2.2.0 # 切换语言版本
$ rvm gemset create gem22 # 创建一个“gem22”的gemset环境
$ rvm use 2.2.0@gem22 # 切换gemset语言，切换首先要保证‘rvm list’命令中显示的，也就是已经安装的
$ rvm gemset list # 列出ruby的gemset
$ rvm gemset empty 2.2.0@gemset22 # 清空一个gemset
$ rvm gemset delete gemset22 # 删除一个gemset
```

## 项目自动加载gemset

在项目中创建文件`.rvmrc`

```bash
$ rvm use 2.2.0@gemset22
```

如此在`cd`今日项目目录时自动加载相应gemset


## bundler

[Bundler](http://bundler.io/)

```bash
$ gem install bundler
```

> bundler打包器，类似于python的pip中requirements; 如果修改了Gemfile这个文件，可以使用`bundle install`来安装所有的gem包，这个命令会检查并安装这些gem包同时生成个Gemfile.lock文件。Gemfile.lock文件会列出当前项目使用的gem套件的具体版本.如果在github克隆一个jekyll项目，要实现本地预览，就要先`bundle install`安装gem包。

## ruby相关站点

- [Ruby](https://www.ruby-lang.org/zh_cn/)
- [RubyGems](https://rubygems.org/)
- [Bundler](http://bundler.io/)
- [Ruby China](https://ruby-china.org/)
