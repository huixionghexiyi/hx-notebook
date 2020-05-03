基础
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

# 插值

- 使用 {{}} 在HTML中插入，Vue({})中data对应的key值。

- 可以使用jS中的单表达式


# 指令

- v-if="key"，如果key在data中存在，只要不是false、null、undefined那么该标签就会被渲染。

- v-bind:[key1]="key2" ，这种是绑定属性名和参数名的方式。只要data中存在key1和key2那么该属性和能被渲染。缺少任意一个都不会被渲染。并且会报错

[key1] 可以写成[key1+key2]的形式，其中key1和key2都是data中的key值，并且为字符串(就是字符串拼接)。

- v-on:click="doThis"，一般用于监听。doThis是一个方法。
参考：https://cn.vuejs.org/v2/api/#v-on
v-on:click.prevent