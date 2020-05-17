# for ... in ...

关键字，`in`运算符，无论该属性是自身的还是继承的都会返回 `true`。显然这这不太合理。引入 **可遍历**的概念，只有可遍历的属性才会被`for ... in `循环遍历。
只要一个属性的 `enumerable`是 `false`，那么就不会取到该属性。

与`Object.keys`类似

# Object.keys

只能获取不可遍历的属性

# Object.getOwnPropertyNames
获取当前对象所有属性

# JSON.stringify

将一个值转换为JSON格式的字符串