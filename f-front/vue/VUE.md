#  Vue

> 前端开发框架，能够组件化开发，声明式渲染，所有的组建都是响应式的：[官方教程]([https://cn.vuejs.org/v2/guide/#Vue-js-%E6%98%AF%E4%BB%80%E4%B9%88](https://cn.vuejs.org/v2/guide/#Vue-js-是什么))


## 基础与概览

`Vue`的教程写得非常详细了，在这里简单的总结回顾一下。在掌握了`JavaScript`的情况下，学习会非常顺利。推荐：阮(读作：软)一峰的书：[《JavaScript 教程》](https://wangdoc.com/javascript/)。

基础内容主要包括**3**个重点：

- `Vue`对象：一切都基于这个对象，可以创建自定义的 `directive`和 `component`；和人这种动物的的相似之处在于，人是由细胞和细胞的分泌物组成的，`VueJS`框架是由`Vue`对象和这个对象的属性组成的。
- `directive`：`v-on`、`v-bind`、`v-model`、`v-if/v-else/v-else-if`、`v-for`
- 自定义组件：你可以将其看作自定义标签，和自定义标签不同的地方是他最终会被`Vue`解析成普通标签。而自定义标签根据：[WebComponents](https://www.w3.org/wiki/WebComponents/)规范编写的直接能被一些浏览器识别的标签。

学习以上**3**点内容，我们就可以先做一些案例，对这些又更深的理解。如果`JavaScript`基础比较好的话，你也可以看了官网的入门之后直接看API。个人认为效率还是挺高的。

然后就是了解`Vue`对象的声明周期等。


## 钩子函数

- bind:只调用一次，第一次绑定到元素时调用
- inserted
- update



- `el`：指令所绑定的元素，可以用来直接操作 DOM。

- `binding`：一个对象，包含以下属性：
  - `name`：指令名，不包括 `v-` 前缀。
  - `value`：指令的绑定值，例如：`v-my-directive="1 + 1"` 中，绑定值为 `2`。
  - `oldValue`：指令绑定的前一个值，仅在 `update` 和 `componentUpdated` 钩子中可用。无论值是否改变都可用。
  - `expression`：字符串形式的指令表达式。例如 `v-my-directive="1 + 1"` 中，表达式为 `"1 + 1"`。
  - `arg`：传给指令的参数，可选。例如 `v-my-directive:foo` 中，参数为 `"foo"`。
  - `modifiers`：一个包含修饰符的对象。例如：`v-my-directive.foo.bar` 中，修饰符对象为 `{ foo: true, bar: true }`。

- `vnode`：Vue 编译生成的虚拟节点。移步 [VNode API](https://cn.vuejs.org/v2/api/#VNode-接口) 来了解更多详情。

- `oldVnode`：上一个虚拟节点，仅在 `update` 和 `componentUpdated` 钩子中可用。