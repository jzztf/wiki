# Nodejs

## nvm(node version manage)


> node的版本管理工具，类似于rvm是ruby的版本管理工具

> 安装nvm

- `curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | sh

## change nvm mirrors

> 修改nvm镜像

`NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node nvm install stable`

## node.js

> 安装稳定版本的node

- `nvm install stable`

## change npm mirrors

> npm类似于python的pip，属于node的包管理工具

- ` npm --registry https://registry.npm.taobao.org install express`

## hexo

- `npm install -g hexo-cli`

or

- `npm --registry=https://registry.npm.taobao.org install -g hexo-cli`

> ps: use "--register option"

## hexo-deployer-git --save

- `npm install hexo-deployer-git --save`

## 相关链接

- [nvm](https://github.com/creationix/nvm/blob/master/README.md)
- [npm](https://docs.npmjs.com/)
- [淘宝npm](https://npm.taobao.org/)

