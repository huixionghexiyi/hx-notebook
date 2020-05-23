# window

`window`只浏览器的当前窗口， `document`指当前窗口的文档内容。

如果你打开一个窗口，不停的在这个窗口里切换网站。其实这个 `window`并没有改变，还是原来的对象。只是 `document`对象在变。

# window的属性

```js
window.name
window.closed // 当前窗口是否关闭
window.opener // 返回一个window对象，即打开当前窗口的父窗口
window.self // 返回当前window对象，只读
window.window // 同上
window.frames // window的别名
window.length
// 其他属性
window.isSecureContext // true 表示 https，false 表示 http
```

## window组件属性
浏览器的组件对象。基本没什么用，都只读
```js
window.locationbar // 地址栏对象
window.menubar // 菜单栏对象
window.scrollbars // 窗口的滚动条对象
window.toolbar // 工具栏对象
window.statusbar // 状态栏对象
window.personalbar // 用户安装的个人工具栏对象
```

## 全局对象属性

```js
window.document // 文档对象
window.location // Location对象，URL相关
window.navigator // 环境对象
window.history // 浏览器浏览记录对象
window.localStorage // 本地存储的local数据
window.sessionStorage // 本地存储的session数据
window.console  // 控制台对象
window.screen // 屏幕信息对象
```

## window对象的方法

```js
 window.alert() // 弹窗
var res =  window.prompt('你叫什么','**笨蛋**') //输入框，获取输入内容，默认笨蛋
var res =  window.confirm() // 确认框，获取结果，确认true，取消false
window.open(url, windowName, [windowFeatures])
window.close('')
window.stop()
// 其他方法
```

## 事件

```js
// load 事件发生在 document加载完毕时触发
window.onload = function(){} // 可以指定回调函数
// error事件，发生在脚本执行错误时
window.onerror = function(message, filename, lineno, colno, error){} //可以指定回调函数,参数分别为：错误信息、出错脚本的网址、行号、列号、错误对象
```