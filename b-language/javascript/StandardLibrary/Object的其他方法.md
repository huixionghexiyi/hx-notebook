# Object的其他方法

- 原型（prototype）对象相关
- getPrototypeOf
- setPrototypeOf
- create
- prototype.isPrototypeOf
- prototype.__proto__
- getOwnPrototypeNames
- prototype.hasOwnProperty

##  getPrototypeOf

获取某实例对象的原型对象

```js
function F() { }
var f = new F()
Object.getPrototypeOf(f) F.prototype // true

// 特殊情况
Object.getPrototypeOf({}) === Object.prototype // true

Object.getPrototypeOf(Object.prototype) === null // true

function f() {}
Object.getPrototypeOf(f) === Function.prototype // true
```

## setPrototypeOf

设置原型对象

```js
function F(){}
var p = {'name':'huixiong'}
var f = new F()
Object.setPrototypeOf(f,p);
f.prototype === p//true
f.name //huixiong
```

`setPrototypeOf` 模拟new函数的功能:
```js
var F = function(){
    this.name = 'huixiong'
}
f.prototype = {a:'b',b:'b'}

var f1 = new F();

var f2 = Object.setPrototypeOf({},F.prototype);//为f2绑定原型
F.call(f2); // 绑定this到构造函数，并且执行这个而构造函数
f1.name // huixiong
f2.name // huixiong
```

## Object.create

```js
// 以下三种等价
var obj1 = Object.create({});
var obj2 = Object.create(Object.prototype);
var obj3 = new Object();
// 创建一个不包含任何属性的对象比如toString，valueOf都没有
var obj4 = Object.create(null);
// 传递第二个参数，属性对象，会自动添加到生成的对象中
var obj5 = Object.create({},{
        p1:{
            value:1, 
            enumerable:true, 
            configurate:true,
            writable:true,
        }
}
});
obj5.p1 // 1
```

## prototype.isPrototypeOf

判断该对象是否为参数对象的原型，只要实例对象在参数对象的原型链上，isPrototype就返回true

```js
var o1 = {};
var o2 = Object.create(o1);
var o3 = Object.create(o2);

o2.isPrototypeOf(o3) // true
o1.isPrototypeOf(o3) // true

Object.prototype.isPrototypeOf([]) // true
Object.prototype.isPrototypeOf({}) // true
Object.prototype.isPrototypeOf(null) // false

```
## prototype.__proto__

返回当前对象的原型对象,即构造函数的prototype属性。

```js
var A = function () { }
var B = function () {
    A.call(this);
}
B.prototype = new A();
B.prototype.constructor = B

var b = new B();
b.__proto__ === B.prototype //true
b.__proto__ === b.constructor.prototype //true
b.__proto__ === Object.getPrototypeOf(b)  //true ,getPrototypeOf是最可靠的方式
```
## 