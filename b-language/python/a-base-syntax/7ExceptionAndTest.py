# 错误处理、调试、测试

#-----------
# 程序出错
# 当try中的代码出错，则不会再执行try下面的代码，直接跳到except中，最后无论无何都会执行finally中的带啊

try:# 可能出现错误的语句快
    r=10/0
    v = 10/int('a')
except ZeroDivisionError as e:# 第一个可能的异常
    print("exception:",e)
except ValueError as e:
    print("valueException",e) # 第二个可能的异常，只有在第一个异常没有捕捉到，第二个异常才有机会捕捉
else:
    print("no error")# 如果没有错误就会执行，不是强制需要
finally:
    print("finally")# 有没有错误都会执行，不是强制需要

# BaseException类是所有异常的父类

# 不同于java，出现错误会自动向调用改函数的方法抛错误，所以只需要在关键地方捕获异常就可以了
# 比较偷懒的就是捕获Exception 这个大异常。如果没有被捕获，就会一直向上抛，知道抛到python解释器

#--------------
# 调试时，看错误栈就好

import logging

def f1(s):
    return 10/int(s)

def f2(s):
    return f1(s)*2

def main():
    try:
        f2('0')
    except Exception as e:
        logging.exception(e) # 将错误的详细情况打印出来。如果不try也会打印详细的错误情况。但是这样就会终端程序了。一般用于调试。(也可以写到日志文件中)
        print("Error",e)
    finally:
        print("finally")
        
main()
print("END")


#--------------
# 抛出错误异常
class F1Error(ValueError):
    pass

def f1(s):
    n = int(s)
    if n==0:
        raise F1Error("invalid value:%s"% s)
    return 10/n

f1('0')

#-----------------
# 调试 ---断言   除了使用print打印错误，最好还是使用assert(断言)

def f1(s):
    n = int(s)
    assert n!=0,'n is zero'# 表示 n!=0 的值是True，不然后面肯定会出错。如果断言出错，会抛出AssertError

f1('0')# 调用

#在程序中导出都是断言，并不会比print好到哪里去。不过可以使用python -O err.py 来关闭断言
# 关闭后，所有的断言都相当于paas


#------------------
#   调试 ---logging ,这才是调试的最终神器
import logging
logging.basicConfig(level=logging.INFO)# 指定记录信息的级别，debug、info、warning、error
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#-----------------
# pdb调试 可以让程序单步运行，感觉不好用，知道有这种东西就好。python -m pdb err.py


#------------------
# 单元测试
# 将要测试的函数放入测试模块中，如果通过测试，就说明没有问题。
# 使用unittest，编写待测试模块，编写测试模块

# mydict.py  实现的是和dict一样的功能
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# mydict_test.py  用于测试Dict的测试单元
import unittest

class TestDict(unittest.TestCase):

    def setUp(self):# 这个方法是在单元测试开始时，执行的方法。比如数据库的连接等。可以写在这里面
        return print("setUp")
    def tearDown(self):# 这个方法在单元测试结束时，执行的方法
        print("tearDown")
    def test_init(self):# 只有以test开头的方法名才会被认为是test方法，一类测试写一个方法就好
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'valueqwf1')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    if __name__ == "__main__":# 这样就可以进行单元测试，加上这句，就可以使用python mydict_test.py 来进行单元测试
        unittest.main()

# 另一种是 python -m unittest mudict_test直接进行单元测试,这样可以一次进行多个单元测试
 
# 单元测试中：setUp()和setDown() 方法可以在测试开始前和结束后执行，例如开关数据库，不必再每个测试中都写重复的连接代码

##
import unittest
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
        def get_grade_right(self): # 这个方法时get_grade修改后的内容
            if self.score < 0 or self.score >100:
                raise ValueError()
            if self.score >= 60 and self.score <80:
                return 'B'
            if self.score >= 80:
                return 'A'
            return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart',80)
        s2 = Student('Bart',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')
        


    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
    
if __name__ == '__main__':
    unittest.main()

#------------------
# 文档测试 doctest模块
# 文档测试就是将测试的内容按照交互式的方式写到注释中，需要包含输入/输出。这样运行时，就会自动提取进行检测。
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':# 这个方法，只有在命令行直接执行的时候才会执行doctest
    import doctest  # 导入这个模块后，就可以使用提取注释中的代码。进行测试。非常明确的写出期望的输出。包括期望的异常。可以用...省略中间的log
    doctest.testmod()

