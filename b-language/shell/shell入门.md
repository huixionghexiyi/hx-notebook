- [简单使用](#简单使用)
- [变量](#变量)
- [运算符](#运算符)
- [流程控制](#流程控制)
- [函数](#函数)
# 简单使用
```sh
#创建一个shell文件
touch helloWorld.sh
# 给文件赋予运行权限
chmod +x helloWorld.sh
#运行shell脚本文件
./ helloWorld.sh 
#如果不用 ./ ,则使用的是PATH下的helloWorld.sh,通常我们的脚本并不在这些目录里，./ 标识表示的是在当前目录下找。
```
# 变量
- shell中变量一般分为三类：
1. 自定义变量：在当前shell中生效，其他shell启动的程序不能访问局部变量。
2. Linux系统中定义的变量（如`$PASH`,`$HOME`,等都可以直接使用）：使用命令`env`可以查看的所有变量。
3. shell变量：shell程序定义的特殊变量。有些是环境变量，有些是局部变量。
- 常用的环境变量：
1. `PATH`决定shell到哪里找命令或程序
2. `HOME`当前用户主目录
3. `HISTSIZE`历史记录数(historysize的简写)
4. `LOGNAME`当前用户的登录名
5. `HOSTNAME`指主机的名称
6. `SHELL`当前用户的shell类型（包括bash、zsh、dash等）
7. `LANGUGE`语言相关的环境变量，多语言可修改此环境变量
8. `MAIL`当前用户的邮件存放目录
9. `PS1`基本提示符，对于root用户是#，普通用户是`$`
- 环境变量的使用：

对文件`helloWorld.sh`进行编辑 
```sh
#！/bin/bash
#使用Linux定义的环境变量,查看当前用户路径
echo $HOME
#使用自定义环境变量
hello="helloWorld!"
echo #hello
```
>注意：在最前面添加`#！/bin/bash`表示使用bash shell来运行，因为linux中存在很多不同的shell，如：zsh shell，dash shell
- `变量名命名`的注意事项：
  - 命名只能使用字母、数字、下划线，首个字母不能用数字开头，可以使用下划线开头
  - 中间不能有空格
  - 不能使用bash中保留的关键字。
- 字符串入门

字符串：(可以使用单引号或者双引号，但是同一个字符串使用统一的符号较好，不然里面的引号会被识别成字符)
```sh
#!/bin/bash
firstName='hui'
lashName='xiong'
name='I am '$firstName'"$lastName"'
# 这里，字符串name中的双引号会被识别成字符
# 输出结果为 I am hui"xiong"
# 赋值时=两边不能有空格哦
```
- 字符串常见操作
拼接字符串：
```sh
name='I am '$firstName''$lastName''
# 无所谓使用单双引号，但是同一个字符串使用一种符号即可。
```
获取字符串长度：
```sh
name='huixiong'
# 第一种方式
echo ${#name}
# 第二种方式
expr length "$name"
```
使用`expr`命令时，表达式两边必须有空格，不然输出表达式本身：
```sh
expr 5+6 # 输出5+6
expr 5 + 6 #输出11
expr 5 \* 6 #有些运算符需要转义才能正确输出
```
- 截取字符串
```sh
str='huixiong is nice man'
echo ${str:0:10}
```
根据表达式截取：
```sh
var="http://www.runoob.com/linux/linux-shell-variable.html"
# %% 找到第一个出现t之前的字符串
# % 找到最后一个出现t之前的字符串
# #*/ 找到第一个/之后的字符串
# #*. 找到第一个.之后的字符串
# ##*/ 找到最后一个/之后的字符串
s1=${var%%t*}#h
s2=${var%t*}#http://www.runoob.com/linux/linux-shell-variable.h
s3=${var%%.*}#http://www
s4=${var#*/}#/www.runoob.com/linux/linux-shell-variable.html
s5=${var##*/}#linux-shell-variable.html
```
- 数组
```sh
arr=(1 2 3 4 5)
#获取长度
len1=${#arr[@]}
len2=${#arr[*]}
输出数组第3个元素
echo ${arr[2]} # 输出数组第3个元素
#删除下标为2的元素，即删除3
unset arr[2]
#遍历输出
for i in ${arr[@]};do echo $i;done
unset arr_number;
```
# 运算符
>运算符比较关键。包括对文件和系统的葛总操作运算。
[菜鸟Shell教程-运算符](https://www.runoob.com/linux/linux-shell-basic-operators.html)
# 流程控制
- if条件语句
```sh
a=3
b=9
if [ $a > $b ]
    echo ""${#a}" 大于 "${#b}""
if [ $a = $b ]
    echo ""${#a}" 等于 "${#b}""    
if [ $a < $b ]
    echo ""${#a}" 小于 "${#b}""    
```
- for循环语句
```sh
# 输出列表中的数据
for loop in 1 2 3 4 5
do
    echo "The value is : $loop"
done
# 产生10个随机数
for i in {0..9}
do
    echo $RANDOM;
done
# 循环输出1到5
for((i=1;i<=5;i++))
do
    echo $i
done
```
- while语句
```sh
int=1
while(($int<=5))
do
    echo $int
    let "int++"
done
```
# 函数
- 不带参数没有返回值的函数
```sh
function f(){
    echo "这是我第一个shell函数"
}
f
fun(){
    echo "这是我的第二个shell函数"
}
fun
```
- 有返回值的函数
```sh
funWithRe(){
    a=3
    b=1
    return $(($a+$b))
}
funWithRe
echo "输入两个数字之和为 $?"
# 如果是单引号，则 $? 需要写成 '$?'
```
- 带参数的函数
```sh
funWthParam(){
    echo "第一个参数为 $1"
    echo "第二个参数为 $2"
    echo "第二个参数为 $10"
    echo "第十个参数为 ${10}"****
}
funWthParam 1 2 3 4 5 6 7 8 9 23 14
#输出结果为 1 2 10 23
# 当参数个数超过10个，就是用 ${10} 来获取值，$10 只能表示 10
```
- 注意

参数 | 说明 
--- |----------
 $# | 传递到脚本的参数个数
 $* | 以一个单字符串显示所有向脚本传递的参数
 $$ | 脚本运行的当前进程ID号
 $! | 后台运行的最后一个进程的ID号
 $@ | 与$*相同，但是使用时加引号，并在引号中返回每个参数。
 $- | 显示Shell使用的当前选项，与set命令功能相同。
 $? |显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。