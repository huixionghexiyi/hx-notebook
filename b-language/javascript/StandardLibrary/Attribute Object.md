# 属性描述对象（Attribute Object）

本质上是一个Object的实例，作为对象的内部数据结构，定义了一些属性，这些属性是描述对象的属性用的。

```js
//一个属性就有如下一个对象来描述,属性描述对象的属性叫做元属性
{
  value: 123,//属性值
  writable: false,//是否可更改value
  enumerable: true,// 如果为false，在迭代是会跳过该属性
  configurable: false,// 为false，该属性的描述对象不可修改
  get: undefined,// 一个函数，表示取值方式
  set: undefined // 表示存值方式
}
```
## 获取属性的描述对象

`Object.getOwnPropertyDescriptor()`:只能获取自身的属性，不可用于继承的属性

```js
var obj = {
    a: 'hello'
}
var b = Object.getOwnPropertyDescriptor(obj,'a')
```
## 定义属性的描述对象

将属性定义为一个对象，该对象就是属性的描述对象。

```js
var obj = Object.defineProperties({}, {
  p1: { value: 1, enumerable: true }, //设置为可枚举
  p2: { value: 2, enumerable: false } //设置为不可枚举
});

Object.getOwnPropertyNames(obj) // ['p1','p2']
Object.keys(obj)// ['p1']

```
## 通过描述对象修改对象的属性

`Object.defineProperty(object, propertyName, attributesObject)`

参数分别为：
1. 属性所在对象
2. 属性名（用字符串表示）
3. 属性描述对象

修改完成后返回更改后的该对象。

`Object.defineProperties(obj, properties)`：一次性修改多个属性，通过描述对象修改。

```js
// 修改一个属性
var obj = Object.defineProperty({}, 'p', {
  value: 1,
  writable: false, //为false，不可修改
  enumerable: true,
  configurable: false
});

obj.p // 1

obj.p = 2;
obj.p // 1 ，无法被修改，静默失败

// 修改多个属性
var obj = Object.defineProperties({}, {
  p1: { value: 123, enumerable: true },
  p2: { value: 'abc', enumerable: true },
  p3: { get: function () { return this.p1 + this.p2 },//定义了get（或set）就不能设置value，不能将writable设置为true
    enumerable:true,
    configurable:true
  }
});
obj.p1 // 123
obj.p2 // "abc"
obj.p3 // "123abc"
```
## 判断某个属性是否可遍历

只能判断自身的属性。

```js
var obj = {};
obj.p = 1;
obj.propertyIsEnumerable('p')

```

## 存取器
指的就是描述对象中的`set`和 `get`。

```js
// 定义一个
var obj = Object.defineProperty({},'p',{
    get: function(){
        return '不允许读取的值'
        },
    set: function(value){
        return '也不允许设置'+ value;
        }
})
obj.p // 不允许读取的值
obj.p = 1// 也不允许设置1
```
存取器的另一种写法：

```js
var obj = {
  get p() {
    return '不允许读取的值';
  },
  set p(value) {
    return '也不允许设置'+value
  }
};
obj.p //不允许读取的值
obj.p = 1 //也不允许设置1
```

## 对象拷贝

- `for ... in`只能获取 `enumerate`为false的属性。所以拷贝不完全
- 可以通过`Object.getOwnPropertyDescriptor`获取属性的描述对象。然后通过`Object.defineProperty`设置。

```js
// 方式一
var extend = function (to, from) {
  for (var property in from) {
    to[property] = from[property];
  }

  return to;
}

extend({}, {
  a: 1
})

// 方式二
var extend = function (to, from) {
  for (var property in from) {
    if (!from.hasOwnProperty(property)) continue;
    Object.defineProperty(
      to,
      property,
      Object.getOwnPropertyDescriptor(from, property)
    );
  }

  return to;
}

extend({}, { get a(){ return 1 } })
```
## 控制对象状态

1. `Object.preventExtensions()`：使一个对象无法再添加属性。可删除和修改。
2. `Object.isExtensible()`：检查一个对象是否使用了前面的方法，也就是判断是否可以添加属性。
3. `Object.seal()`：无法添加新属性，也无法删除旧属性（实质使将描述对象的 `configurable`设置为`false`），不影响修改，这是因为值的修改由 `writable`决定。
4. `Object.isSealed()`：判断是否使用了前面的方法。同时： `isExtensible`也为false
5. `Object.freeze()`：使一个对象无法添加，删除，修改一个属性。此时对象就变成了常量。
6. `Object.isFrozen()`：判断是否使用了前面的方法。若为false，上面两个判断也为false

> 虽然有了上面三种限制，但是可以通过改变原型对象来为对象增加属性。

```js
var obj = new Object();
Object.preventExtensions(obj);

var proto = Object.getPrototypeOf(obj);// 获取Object的实例的原型
// Object.preventExtensions(proto); //将冻住原型就可以防止被修改了。
proto.t = 'hello';
obj.t

```

> 如果属性是对象的话，那么只能冻住执行这个对象的指针。这个指针不能指向其他对象。但是可以修改这个对象
```js
var obj = {
  foo: 1,
  bar: ['a', 'b']
};
Object.freeze(obj);

obj.bar.push('c');
obj.bar // ["a", "b", "c"]
```
总结主要方法：

- getOwnPropertyDescriptor:获取自身属性的描述文件，2个参数分别是：对象，属性名
- getOwnPropertyNames：获取对象的所有属性，1个参数：对象
- defineProperty：设置属性，三个参数，属性所在对象，属性名，描述对象
- defineProperties：设置多个属性，2个参数，属性所在对象，包含描述对象的对象。
- preventExtensions：不可添加属性。
- isSealed：不可添加和删除属性。
- freeze：不可添加、删除、修改属性。