# Node.js

浏览器提供了一个`JavaScript`编译环境，可以在前端实现一些复杂的功能。而`Node.js`提供了后端的`JavaScript`环境。通常`node.js`用来优化前端开发的开发体验。比如：压缩js、img、css等。这些功能都是通过`js`提供，当然你也可以使用`java`来做这些工作，但是这些功能一般都是前端工程师在做，而前端工程师总是愿意使用`js`的。



## nvm

`node.js`有许多版本，而不同的版本很可能出现不同的兼容问题，主要是js编译器和js包管理器不同。所以，有这样的需求，那总有人去开发一个`nvm`。

请到官网去安装：[官方github](https://github.com/nvm-sh/nvm#installing-and-updating)

```shell
nvm install node:安装最新node.js

nvm install [version]:安装指定版本node.js

nvm use [version]:使用指定版本

nvm list :列出当前安装的所有node

nvm uninstall [version]:卸载指定版本的node

nvm node_mirror [http://npm.taobao.org/mirrors/node]:设置nvm镜像。应对下载想要的版本过慢的问题。

nvm npm_mirror [https://npm.taobao.org/mirrors/npm/]:设置npm的镜像
```



## npm

node.js的包管理工具，是`node.js`的一部分，里面有很多别人提供的非常好用的前端开发框架，例如：`webpack`、`vue`、`babel`等。

### 常用命令：

```shell
`npm init` 初始化前端项目，手动初始化，需要填一些参数
`npm init --yes` 默认初始化配置
`npm -v`  查看npm版本，与nvm是对应的。
`npm install [package]` 安装对应的包,在当前路径下，可以通过require()来引用js,是node.js提供的方法
`npm install [package] -g` 安装到当前node环境中。可以在cmd中当作命令使用
`npm install [package] --save-dev` 安装package到开发环境，生产环境不会安装。
`npm uninstall [package]` 卸载包
`npm update [package]` 更新包
`npm search [package]` 搜索包
`npm install -g cnpm -registry=https://registry.npm.taobao.org` 使用淘宝镜像安装包
以后就使用cnpm来安装包
cnpm install [package]
```



## 创建一个node.js项目

初始化当前目录为一个node项目，里面会生成一个package.json文件，是node项目的主要配置文件

```
npm init
```

