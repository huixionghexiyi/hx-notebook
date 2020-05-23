# 面向对象

- [面向对象](#%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1)
  - [什么是对象](#%e4%bb%80%e4%b9%88%e6%98%af%e5%af%b9%e8%b1%a1)
  - [构造函数](#%e6%9e%84%e9%80%a0%e5%87%bd%e6%95%b0)
  - [`new`关键字](#new%e5%85%b3%e9%94%ae%e5%ad%97)
  - [根据实例对象创建实例对象](#%e6%a0%b9%e6%8d%ae%e5%ae%9e%e4%be%8b%e5%af%b9%e8%b1%a1%e5%88%9b%e5%bb%ba%e5%ae%9e%e4%be%8b%e5%af%b9%e8%b1%a1)
  - [`this`关键字](#this%e5%85%b3%e9%94%ae%e5%ad%97)
  - [使用 `this` 注意](#%e4%bd%bf%e7%94%a8-this-%e6%b3%a8%e6%84%8f)
    - [避免多层使用this](#%e9%81%bf%e5%85%8d%e5%a4%9a%e5%b1%82%e4%bd%bf%e7%94%a8this)
    - [避免在数组的实例方法中使用this](#%e9%81%bf%e5%85%8d%e5%9c%a8%e6%95%b0%e7%bb%84%e7%9a%84%e5%ae%9e%e4%be%8b%e6%96%b9%e6%b3%95%e4%b8%ad%e4%bd%bf%e7%94%a8this)
    - [避免回调中使用this](#%e9%81%bf%e5%85%8d%e5%9b%9e%e8%b0%83%e4%b8%ad%e4%bd%bf%e7%94%a8this)
  - [绑定this的方法](#%e7%bb%91%e5%ae%9athis%e7%9a%84%e6%96%b9%e6%b3%95)
  - [原型（prototype）对象](#%e5%8e%9f%e5%9e%8bprototype%e5%af%b9%e8%b1%a1)
    - [原型链](#%e5%8e%9f%e5%9e%8b%e9%93%be)
    - [constructor属性](#constructor%e5%b1%9e%e6%80%a7)
    - [构造函数的继承](#%e6%9e%84%e9%80%a0%e5%87%bd%e6%95%b0%e7%9a%84%e7%bb%a7%e6%89%bf)
    - [多重继承](#%e5%a4%9a%e9%87%8d%e7%bb%a7%e6%89%bf)
  - [模块](#%e6%a8%a1%e5%9d%97)
## 什么是对象
对象是对现实生活中实物的抽象。

对象是一个容器，封装了属性和方法。属性描述对象状态，方法赋予对象行为。

## 构造函数

不像 `java`，js没有class来定义一个对象。一个函数就可以看成是一个类，在js中叫构造函数。为了区分构造函数和其他函数，构造函数通常首字母大写。

如果函数中包含 `this`字段，则会被认为是构造函数。

```js
var Car = function() {
    this.price = 1000;
    
}
function Cat(name){
    this.name = name;
}
var car_1 = new  Car();
car cat_1 = new Cat();
```
`this`指向当前实例， `new`用来根据构造函数生成实例。如果没有new命令，将表示调用这个函数，而不是生成一个实例。


## `new`关键字

1. 创建一个空对象，作为将要返回的对象实例
2. 将空对象的原型 `__proto__`，指向构造函数的 `prototype`属性
3. 将这个空对象赋值给函数内部的 `this`关键字
4. 执行构造函数内部代码

若构造函数返回的是一个对象（{a:1}），则返回这个对象，否则就不理睬这个return语句。

## 根据实例对象创建实例对象

有时候我们只有实例对象，想要新建一个实例对象，就需要用到 `Object.create()`方法。

```js
var person1 = {
  name: '张三',
  age: 38,
  greeting: function() {
    console.log('Hi! I\'m ' + this.name + '.');
  }
};

var person2 = Object.create(person1);

person2.name // 张三
person2.greeting() // Hi! I'm 张三.
```

## `this`关键字

this总是返回一个对象。this是属性和方法当前所在的对象。也就是当前的上下文环境（context）

```js
function fun(){
  return this.msg;
}

var a = {
  'msg': 'im a',
  'f':fun
}
var b = {
  msg: 'im b',
  f:fun
}
var c = {
  'msg': 'im c',
  'f': a.f
}
console.log(a.f()) //im a
console.log(b.f()) //im b
console.log(c.f()) //im c
```
我们可以这样理解，在js中如果是对象赋值给变量。那么，变量存的其实是对象的内存地址。在c中，`a.f`表示的是一个地址，将这个地址传给了c。所以当c调用方法 `f`的时候。会直接通过地址找到这个函数,所以上下文就是对象c。

## 使用 `this` 注意

### 避免多层使用this
### 避免在数组的实例方法中使用this
### 避免回调中使用this

## 绑定this的方法
2020年5月15日


## 原型（prototype）对象

通过`构造函数`创建的`实例`无法共享属性。这样造成了资源的浪费。所以引入`prototype`原型对象。凡是定义在 `prototype`上的属性，都会被所有实例共享。 `prototype`本质上是一个 `object`。

```js
function Animal(name) {
  this.name = name;
}
Animal.prototype.color = 'white'; // 定义在原型上的属性，共享

var cat1 = new Animal('大毛');
var cat2 = new Animal('大毛');
var cat3 = new Animal('二毛');
cat3.color = 'red';

cat1.color // 'white'
cat2.color // 'white'
cat3.color // 'red'   // 自身有的属性就不会去原型上找
cat1.name === cat2.name // false 不是定义在原型上的属性，不共享
```
在上例中，如果实例对象有 `color`属性，那么就不会去找。

### 原型链

js中，任何对象都有自己的原型对象，也可以充当其他对象的原型。由于原型对象也是对象，所以他也有自己的原型。请看下面的例子：

```js
var Animal = function(){}
Animal.prototype.name = 'anyone'

var Cat = function(){}
Cat.prototype = new Animal();
Cat.prototype.constructor = Animal;
var cat1 = new Cat();
var cat2 = new Cat();
cat1.name //anyone
cat1.name === cat2.name //true
cat1 === cat2 // false
```
案例中，Animal的原型（prototype）中定义个属性name；定义一个构造函数Cat，Cat的原型指向一个Animal实例（new创建实例）；Cat原型中的constructor属性指向Animal，然后Cat的实例cat1就能使用Animal中的属性和方法。

如果没有找到，最终会找到Object上的原型，看看Object.prototype上有没有这个属性，如果也没有，会找prototype上的constructor所在的构造函数，发现为 `null`，就返回没有找到。

可以通过 `实例名 instanceof 构造函数名` 来检查，某个实例是不是构造函数构造出来的。本质是检查右边构造函数的 `prototype`是否在左边实例的原型链中。

### constructor属性

`constructor`属性是在 `prototype`上的，所以能被所有实例继承和共享，指向`prototype`所在的构造函数。所以能通过实例的 `constructor`属性判断，该实例是哪个构造函数创建的。

作用：指明该实例是哪个构建函数创建的；表示原型对象和构建很熟的关系；可以通过实例的这个属性创建另一个实例。

使用constructor创建实例：

```js
function Class(){}
var x = new Class();
var y = new x.constructor();
y instanceof Class //true
```

如果我们要修改一个构造函数的 `prototype`那么最好也修改 `prototype.constructor`，保证原型和实例一致。

### 构造函数的继承

让一个构造函数继承另一个构造函数中的所有属性，并且可以自定义一些属性。

```js
var A = function(){
  this.msg = 'instance msg'
}
A.prototype.msg = 'proto msg'
var B = function(){
  A.call(this); // 相当于调用A方法，也就是将A中的代码放到B中来执行,也就是继承了A中的msg属性
}
B.prototype = Object.create(A.prototype);// 将A的原型的实例赋值给B的原型（也就是在内存中创建一份一样的对象）
B.prototype.constructor = B; // 指定构造方法为
var b = new B();
b.msg // instance msg
```
只继承指定prototype方法：
```js
B.prototype.print = function(){
  A.prototype.print.call(this);
}

```

### 多重继承

```js
function M1() {
    this.hello = 'hello'
}
function M2() {
    this.world = 'world'
}
function S() {
    M1.call(this);
    M2.call(this);
}

S.prototype = Object.create(M1.prototype);
Object.assign(S.prototype, M2.prototype);

S.prototype.constructor = S;

var s = new S();
console.log(s.hello + s.world) // 这就继承了M1中的hello 和M2中的world属性，已经他们的prototype对象
```

## 模块



模块是实现特定功能的一组属性和功能的封装。

在ES6中有了比较好的实现，这里的模块实现，大致了解就好。

```js
// 方式一： 直接封装为一个对象，但是外界也可以修改里面的方法和属性
var Module1 = new Object({
  m1: function(){},
  m2: function(){},
})
// 方式二： 设为私有属性，即不绑定为方法的属性。外界就无法修改了。
// 但由于私有变量存在于构造函数中，所以该构造函数会一直存在，占用内存。
var Module2 = function(){
  var arr = [];
  this.add = function(val){
    arr.push(val);
  }
  this.toString = function(){
    return arr.join(",");
  }
}
// 方式三：基于方式二改进，方法都在prototype对象中，私有变量在实例中。
// 与方式一有同样的问题，就是外界能直接访问属性arr
var Module3 = function () {
    this.arr = [];
}
Module3.prototype = {
    constructor: Module3,
    add: function (val) {
        arr.push(val);
    },
    toString: function () {
        return arr.join(",");
    }
}
// 方式四：立即执行函数;外界无法获取到arr，只能获取到提供的两个方法。
var Module4 = (function () {
    var arr = [];
    var add = function (val) {
        arr.push(val);
    }
    var toString = function () {
        return arr.join(",");
    }
    return {
        add: add,
        toString: toString
    }
})();
```

