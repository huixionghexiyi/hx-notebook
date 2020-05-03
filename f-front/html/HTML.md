# **HTML**

> 这里只是基本的概念指南，网上已经有了非常丰富的内容，就不重复画轮子。在看完本文理解概念之后。请参考菜鸟教程：[HTML文档](https://www.runoob.com/tags/ref-byfunc.html)

基本结构：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>我的第一个标题</h1>
</body>
</html>
```
## **基本概念**

### **行级标签与块级标签的区别：**

| 行级标签                                           | 块级标签                                         |
| -------------------------------------------------- | ------------------------------------------------ |
| 默认宽度由内容撑开(内容多宽、宽度就占多宽)；       | 默认宽度100%(占满一行)；                         |
| 行级标签不会自动换行(一行当中，从左往右依次排列)； | 块级标签自动换行(独占一行，右边不能有任何东西)； |
| 行级标签的宽度高度不能设置！                       | 块级标签可以使用CSS设置宽度高度！                |

## **属性**

每个标签可以添加属性，有些属性是标签独有的，需要针对某一个标签单独去查看。有些属性是所有标签共有的，请参考：[全局属性](https://www.runoob.com/tags/ref-standardattributes.html)

### **事件**

窗口的变化，鼠标，键盘的操作，都可以添加事件，然后触发一段javascript脚本。事件可以添加到任意标签上。事件文档请参考： [HTML事件](https://www.runoob.com/tags/ref-eventattributes.html)

### **其他**

- **HTML和JavaScript的关系：**

JS是一门语言，他需要运行环境来编译语言。类chrome都提供了`V8`引擎，也就是js的运行环境。同时。浏览器将整个页面转换为`document`对象，代表整个`html`文档。而其中的标签则转换为`Element`对象，提供给JS用于操作。

多提一句，一个窗口浏览器也被转换为了`window`的js对象。js可以直接操作。

- **HTML与CSS的关系：**

CSS的目的是改变标签的样式，也就是修改`style`属性的值。

- **HTML5提供了更多的东西：**
  - [画布](https://www.runoob.com/tags/ref-canvas.html)：通过js脚本调用`<canvas>`的`getContext("2d")`对象绘制2D图像
  - [音/视频](https://www.runoob.com/tags/ref-av-dom.html)：调用`<audio>`和`<video>`提供的方法来播放视频，这也是`flash`逐渐被淘汰的原因

## 其他
搜索引擎优化（从搜索引擎中搜索到该页面时，优化浏览器的显示内容）：

```html
<!-- 定义字体等信息 -->
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">

<!-- 定义关键字，告诉搜索引擎，这个网站是干嘛的。能提高搜索命中率 -->
<meta name="Keywords" content="网易,邮箱,游戏,新闻,体育,娱乐,女性,亚运,论坛,短信" />

<!-- 搜索引擎优化 -->
<meta name="Description" content="网易是中国领先的互联网技术公司，为用户提供免费邮箱、游戏、搜索引擎服务，开设新闻、娱乐、体育等30多个内容频道，及博客、视频、论坛等互动交流，网聚人的力量。" />
```









