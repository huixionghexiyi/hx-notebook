#  Vue

> 前端开发框架，能够组件化开发，声明式渲染，所有的组建都是响应式的：[官方教程]([https://cn.vuejs.org/v2/guide/#Vue-js-%E6%98%AF%E4%BB%80%E4%B9%88](https://cn.vuejs.org/v2/guide/#Vue-js-是什么))


## 基础

1. 实例 
2. 组件 
3. 指令 
4. 选项 
5. 模板渲染 
6. 事件绑定 
7. 计算属性 
8. 内置动画 
9. 组件交互 
10. 内置路由 


- [X]  安装部署
- [X]  数据与方法
- [X]  模板语法-插值
- [x]  模板语法-指令
- [ ]  class与style
- [ ]  条件渲染
- [ ]  列表渲染
- [ ]  事件绑定
- [ ]  表单输入绑定
- [ ]  组件基础
- [ ]  组件注册
- [ ]  单文件组件


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