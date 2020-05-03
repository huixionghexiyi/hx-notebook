/**
 * 错误的三个参数
 * message:错误信息
 * name:错误名
 * stack:错误栈
 */

/**
 * 捕获错误
 */
function throwIt() {
    throw new Error('抛出一个错误')
}
function catchIt() {
    try {
        throwIt();
    } catch (e) {
        console.log(e.name + '==' + e.message)
        console.log('===')
        console.log(e.stack)
    }
}
catchIt()

/**
 * 其他错误类型
 * SyntaxError：语法错误
 * ReferenceError：引用一个不存在的对象。或 等号左边不是一个变量
 * RangeError：Array参数超出范围，Number对象的方法参数超出范围，函数堆栈超出最大值。
 * TypeError：类型错误
 * URIError：URI相关函数不正确时抛出,包括：encodeURI()、decodeURI()、encodeURIComponent()、decodeURIComponent()、escape()和unescape()
 * EvalError: eval函数没有被正确执行时抛出，已经弃用。为了兼容还保留着
 */

/**
 * 自定义错误
 * protytype = new Error() 即可继承Error
 * 在将constructor方法改成自身
 */
function UserError(message) {
    this.message = message || '默认错误信息';
    this.name = 'UserError';
}
UserError.prototype = new Error();
UserError.prototype.constructor = UserError;
new UserError('这是一个自定义错误')

/**
 * throw
 * 手动中断程序，并抛出错误
 * 可以抛出任意类型
 */
if(x>1){
    throw new Error('2>1了')
}

/**
 * try/catch
 * 捕获异常程序正常进行，否则程序终端
 * 不同异常不同的处理
 * finally，无论try中是否有异常、是否return，或者是否有catch，都会执行finally里的语句
 * try/catch/finally可以嵌套
 */
try{
    throw 123
}catch(e){
    console.log(e)
}

try{
    foo.bar();
}catch(e){
    if(e instanceof EvalError){
        console.log('EvalError:'+e.name+':'+e.message)
    }else if(e instanceof RangeError){
        console.log('Range'+e.name+':'+e.message)
    }
}finally{
    console.log('清理工作完成')
}