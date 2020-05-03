/**
 * console 是JS的原生对象
 */

/**
 * console 的静态方法
 */

console.log('log1', 'log2', 'log3')
console.info('info1', 'info2', 'info3')//与log用法一样
console.debug('%s + %s = %s', 1, 2, 3)// 显示级别在verbose才会显示


/**
 * %s 字符串
 * %d 整数
 * %i 整数
 * %f 浮点数
 * %o 对象链接
 * %c CSS格式字符串
 */
console.log('%d--%d', 'red')
console.log('%d--%d', 11 + 8)
console.log('%s--%s', 'red')
console.log('%s--%s', 11 + 8)
console.log('%d--%d', 3.14 * 2)
console.log('%f--%f', 3.14 * 2)

console.log('%cThis text is styled!',
    'color: red; background: yellow; font-size: 24px;')//在浏览器生效

/**
 * 参数是对象，显示值
 * 若有构造方法，返回构造方法
 */
console.log({ 'a': 'value' });
console.log(Date);
console.log(function () { });

/**
 * console所有方法都可以被覆盖
 */

['log', 'info', 'warn', 'error'].forEach(function (method) {
    console[method] = console[method].bind(
        console, new Date().toISOString()
    );
});
console.error('出错了')

/**
 * warn 浏览器中有黄色 警告
 * error 浏览器中有红色警告
 * table 将复合类型转换为表格
 */
var languages = [
    { name: "JavaScript", fileExtension: ".js" },
    { name: "TypeScript", fileExtension: ".ts" },
    { name: "CoffeeScript", fileExtension: ".coffee" }
];
var languages = {
    csharp: { name: "C#", paradigm: "object-oriented" },
    fsharp: { name: "F#", paradigm: "functional" }
};
console.table(languages);

/**
 * conunt
 * 输出它被调用了多少次
 */
function g(){
    console.count('f');
}
g()
g()
g()
/**
 * dir :检查一个对象，易于阅读和打印
 * dirxml：以目录形式显示DOM节点
 * assert: 用于调试，
 * time: 和参数相同的timeEnd为一对
 * timeEnd: 和参数相同的time为一对
 * 
 */
// console.dir(document.body) // 浏览器中才能执行
a = 1
console.assert(a>10,'A必须大于等于10 哦~')

console.time('Array initialize')
var a = Array(10000);
for( var i=0;i<10000;i++){
    a[i] = i;
}
console.timeEnd('Array initialize')

/**
 * group
 * groupEnd
 * groupCollapsed
 * trace
 * clear
 */

/**
 * 浏览器端
 * $_ 返回上一个表达式的值
 * $0 -$4 控制台保存了最近选择的Elements面板中的元素，$0表示第一个
 * $(selector) 返回第一个匹配的元素，等于document.querySelector()
 * $$(selector) 返回选中的DOM对象，等于document.querySelectorAll
 * $x(path)
 * 
 */

 /**
  * debugger
  */
