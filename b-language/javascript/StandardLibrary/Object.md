# Object Guide

`Object`是最基础的数据类型中的一种。可以看成是`对象`这种原始数据的的的一种`包装对象`，可以构造出一个`对象`。就像其他数据类型的`包装对象`一样。

> *包装对象*用于给`原始数据类型`提供更多方法

我们常看到的 `json`格式的字符串，其实就是 `JavaScript Object Notation`，即`js对象表示法`。就是最开始用来描述js的对象的。

Object可以将任意类型转换为`对象`。（类似于`Number`封装函数只可以将数字转换为数字对象，通过这个数字对象可以操作这个数字，这些内容可以在其他`Number`中查看）

1. `__proto__`: 根据定义，__proto__ 是该对象(`Object`)的原型(`prototype`)的构造函数(`constructor`)引用。
2. `prototype`：该属性上定义的方法在当前对象的实例中可以直接调用
3. `constructor`：有这个属性的对象才能创建实例。2020年5月14日

`A instanceof B`: 在A的原型链上找B的构造函数`constructor`

![Object和Function的关系](./../Object和Function的关系.jpg)

## Object本身方法（构造函数本身独享的方法实例无法调用）

```js
Object.print = function (o) { console.log(o) };
Object.print()

// 自定义对象都是Object的实例
var Animal = function(){}
Animal.yap = function(name){
    console.log(name)
}
Animal.yap('wangwangwang')
```
## Object实例方法

绑定在属性 `prototype`上的方法。

## Object()函数

根据上面的图，我们可以知道，