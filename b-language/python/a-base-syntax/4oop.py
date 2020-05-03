
# 在python中，所有数据类型都可以看成是对象

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


    def printName(self):
        print(self.name)


    def printGender(self):
        print(self.gender)


ldh = Student('liudehua','女')
ldh.printGender()

#-------------------------------------------
# 给实例强制绑定name属性
class Person(object):
    # 类似于java中的构造方法,__init__时一个相当于构造方法。不同的是第一个参数必须是self
    # 创建了该方法后,如果还有其他参数，必须传递。
    # 单下划线，可以被外界访问。但是请将他看成private，不要随意访问。
    _var1 = []
    # 双下划线。不能被外界访问，原因是被Python解释器对外修改成了_Person__var2,任然可以访问这个变量名。
    __var2 = "鳄鱼皮"
    def __init__(self):
        pass
    # 于普通函数不同的是，类中的函数的第一个参数必须是self
    def method(self,nice):
        pass


p = Person()
p.name = '中文'
print(p.name)
# 虽然__var2是私有的,但是这样不会报错，原因是相当于给实例强制新增了一个外部变量名为：__var2的属性
print(p._Person__var2)
p.__var2 = '垃圾桶'
print(p.__var2)

#------------------------------------------------
#------------------------------------------------
# 继承/多态
# 继承
# 类似于java，一个类继承另一个类的时候拥有另一个类的所有方法，但是可以对齐进行重写。
class Animal(object):
    def run(self):
        print("Anmial is running")

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(object):
    def run(self):
        print("Cat is running")

a = Animal()
d = Dog()
c = Cat()

# 再定义一个方法执行两次run方法
def run_twice(Animal):
    Animal.run()
    Animal.run()
# 这里很好的体现了多态和继承
run_twice(d)

# 但是与静态语言不同的是，传递的方法可以不是Anmial，因为Anmial也是继承object的，而所有的类都继承它，所以也是一种多态的表现。
# car 只需要有个run方法就可以了

class car(object):
    def run(self):
        print("car is running")

run_twice(car())

#-------------------------------------------
# 获取对象信息
# 查看一个变量的类型
print(type(123))
# 查看一个函数的类
print(type(abs))
# 所以如下返回True
print(type(123)==int)
# 判断一个对象是否是函数，可以使用types模块中的变量
import types
def fn():
    return 1
print(type(fn)==types.FunctionType)# FunctionType 是所有函数的基类

# 使用 isinstance
# 能够判断一个实例是否是指定的class的实例
# 可以将继承关系看成一个树。如果直线向上找。能找到，那么就返回True。
class a0(object):
    pass

class a1(a0):
    pass
class a2(a0):
    pass
class b0(object):
    pass
class b1(b0):
    pass
# 上面5个class看成一棵树
a = a1()
b = b1()

print(isinstance(a,a0) and isinstance(b,b0))
# false a对应的类，向上找，找不到对应
print(isinstance(a,a2))
# object 是所有类的基类
print(isinstance(b1,object))
# 判断某个类型是否是某些类型中的一种。
isinstance([1,2,3],(list,tuple))


# 使用dir获取一个对象的所有属性和方法
print(dir('ABC')) # 返回str 的所有方法和属性

# 其他
# 形如__xxx__() 的方法都是有特殊用途的
len('ABC') # 返回长度,本质是len()函数调用其内部的__len__() 方法
'ABC'.__len__() # 与上诉方法相同

# 如果自己写的class也想使用 len(MyClass) 这样的方法，可以自己定义一个 __len__() 方法
# hasattr、setattr、getattr方法的使用
class Car(object):
    def __init__(self):
        self.wheel = 9
    
    def power(self):
        return self.wheel*self.wheel
        


car = Car()
hasattr(car,'wheel') # 有wheel这个属性 True
setattr(car,'door',4)# 设置door这个属性 
get1 = getattr(car,'door')
get2 = getattr(car,'boy',404)# 获取属性boy 如果不存在返回404
print(get1)
print(get2)
print(car.door)
# 当然，类中的方法也是属性
#####  使用：这三个方法的使用，一般用来判断一个对象中是否有想要的方法或者属性。如果有再执行某些操作,如下：
def drive(car):
    print("有oil, 可以开车")

def driver_car(car):
    if hasattr(car,'oil'):
        return drive(car)
    else:
        print('开不了')
    return None
setattr(car,'oil',True)
driver_car(car)
#---------------------------
# 实例属性和类属性
# __init__中声明的属性是实例属性
class Student(object):
    count = 1
    gender = 'boy'# gender是属于类的
    def __init__(self, name):
        self.name = name
        self.count+=1

# 这里Bob传递给name属性，属于实例
s = Student("Bob")
print(Student.count)
print(s.count)# 实例没有这个属性，那么就返回类的这个属性
sb = Student("Mary")
print(sb.count)# 属于类的所以返回2
# 这里的score也是属于实例的属性
s.score = '90'
s.gender = "girl"# 调用
Student.nice = True
print(Student.nice)

del s.gender # 删除一个实例的属性


# ----------------
# 面向对象高级编程 
"""
- 除了给实例绑定一个属性外。还可以绑定方法
- 使用slots来限制绑定的方法或属性。
"""
class Student(object):
    pass

s = Student()
s.name = 'huixiong' # 绑定属性

#定义一个方法，让实例s去绑定
def get_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(get_age,s) # 给实例绑定一个方法，需要使用MethodType方法传递一个方法类型给set_age。（自己猜的）
s.set_age(33)
print(s.age)# 强调:方法是属于实例的，不属于类，另一个实例没有此方法

# 给class绑定方法后，所有的实例都可以调用

# 定义一个方法让class绑定
def set_score(self,score):
    self.score = score

Student.set_score = set_score # 给class绑定方法就不需要使用MethodType

#---------------
# 限制class的实例能添加的属性
# 并且只对实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__=('name','age')# 特殊属性，slots中文意思是插槽，很形象。又是传递tuple，很容易想到是用于限制的

s = Student()
Student.nice = True # 只针对实例，类是可以绑定的
print(Student.nice)
s.name = 'huixiong'
s.age = 19
# s.score = 99 # 这里会报错AttrubuteError，因为没有绑定在slots中。

class BoyStudent(Student):
    # 如果定义该变量，则集成父类的 __slots__中的限制
    __slots__ = ('face_value')# 这里的slots再加上父类的slots就是BoyStudent的slots
    pass

bs = BoyStudent()
bs.name = 'huixiong'
bs.face_value = 100
bs.face_value = 100
print(bs.name)
print(bs.face_value)

"""
- 使用property来将一个方法变成属性调用。
- 这样就不用写get/set方法就能对属性进行验证等操作
"""

class  Student(object):

    @property
    def score(self):
        return self._score # 回忆一下，属性名为 _XX 的表示不建议直接调用。

    # 进行验证
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError(" score must be an interger! --by hx")
        if value <0 or value>100:
            raise ValueError("score must between 0~100")
        self._score = value

    # 虽然很不科学，性别只能是 男 
    # 如果不定义setter方法就只是一个只读属性
    @property
    def gender(self):
        return u'男'


s = Student()
s.score = 60 # 实际上是s.set_score()
s.score #实际上是转化为s.get_score()
print(s.gender)
s.gender = '女' # 没有定义setter，所以只能获取，不能修改

#----------------------
#多重继承
# 一个类可以同时继承多个类，java中没有多继承。但是c++、c#中都是有多继承的

class Mammal(object):# 哺乳动物
    pass

class Bird(object):# 鸟类
    pass

class RunnableMixIn(object):# 混入MixIn的名字，可以让我们方便看出这是混入的额外功能类。
    pass

class FlyalbeMixIn(object):
    pass

class Dog(Mammal,RunnableMixIn):
    pass

class Parrot(Bird,FlyalbeMixIn):# 鹦鹉
    pass

# 在设计的时候，我们可以优先考虑组合多个MixIn功能来达到继承的要求。而不是分层。

#--------------
# 如果想让控制台直接输出变量,可以自定义可以重写 __str__ 方法。(这个方法在object中存在)
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):# 使用print直接打印的时候可以直接输出这段内容。而不是<__main__.Student object at xxxx>类型
        return "Student name is %s"% self.name
    
    __repr__ = __str__
    # def __repr__(self):# 不使用print就能直接打印在控制台，一般用于调试。通常是和__str__是相同的。使用__repr__ = __str__
    #     return   __str__()  # 这里这样使用也可以

s = Student('huixiong')
print(s)

#------------
# __iter__
# 重写这个方法可以让这个类变成可迭代对象，可以使用for in 。该方法返回一个迭代对象，然后python的for就能不断调用该迭代对象的__next__()方法拿到下一个值。
class Fib(object):
    
    def __init__(self, *args, **kwargs):
        self.a,self.b = 0,1

    # def __iter__(self):# 实例本身就是迭代对象，故返回自己
    #     return self
    
    # # 当然也需要重写next
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b # 即a=b,b=a+b
        if self.a>100:
            raise StopIteration()
        return self.a

    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        print('__getitem__')
        return a
from collections.abc import Iterable,Iterator
f = Fib()
print(isinstance(f,Iterable)) # 即是迭代器 Iterator(实现了__next__)，也是可迭代对象 Iterable(实现了__getitem__)
for n in Fib():
    print(n)

#-----------------------
# __getitem__
# 要想使其能像list那样通过下标输出。
class Fib(object):

    def __getitem__(self,n):# 实现这个方法就能实现通过下标来获取参数
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib()
print(f[2])

#-----------------------
# 自制切片，__getitem__()传入的可能是一个int或slice，所以要做判断

class Fib(object):

    def __getitem__(self,n):# 实现这个方法就能实现通过下标来获取参数
        if isinstance(n,int): # n是索引
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):# n 是切片
            start = n.start # 开始
            stop = n.stop   # 结束
            if start is None:# 如果开始索引不存在
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

# 但是step还没有设定，所以f[:10:2]就相当于[:10]
# 同时也没有对负数进行处理。
# 扩展：对应的方法有__setitem__()、__delitem__()。通过这些方法，我们自定义的方法和官方可迭代对象没有区别。
# -------------------------

# ----------------------
# __getattr__ 当我们调用一个对象的属性时，如果属性不存在会报错。
# 但是我们可以通过__getattr__方法修改
class Student(object):

    def __init__(self, *args, **kwargs):
        self.name = 'huixiong'
    
    def __getattr__(self,attr):# 如果调用的方法不存在是会调用__getattr__
        if attr == 'score':
            # return lambda:20 # 当然也可以返回一个函数(lambda是匿名函数)
            return 100
        raise AttributeError("Student has no attr %s"%attr)# 这样在调用没有响应的方法时报错。不然的话就会返回默认的None

s = Student()
print(s.score())

## getattr的重要使用，动态匹配URL

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain("%s/%s"%(self._path,path))# 仔细理解这个方法。

    def users(self,path):# 有bug 不太对。 参考链接https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
        return Chain("%s/users/%s"%(self._path,path))

    def __str__(self):
        return self._path

print(Chain().users('huixiong').qwr.fuck.myname.users('huixiong2'))# 如果时这样会换行,再次输出

#---------------
#使用枚举类

# 常量可以用大写字母来表示，但是其本身任然是变量，是可能被修改的。
JAN = 1
NAME = 'huixiong'
# 最好时使用枚举类定义一个class，每个常量都是class的唯一实例
from enum import Enum
Month = Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May',
     'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 枚举所有的成员
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

# 这样可以更精确的控制枚举的类型
from enum import Enum,unique

# 更精确的指定枚举的类型
# 可以指定任意类型和任意值
# 指定后就不能修改
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Sun
print(day1.value)# 获取周一
print(Weekday.Tue) # 获取周二
print(Weekday['Tue']) # 获取周二
print(Weekday.Tue.value) # 获取周二的值
print(day1 == Weekday.Mon) #True
print(Weekday(1)) # 获取周一
# 遍历
for name,member in Weekday.__members__.items():
    print(name,'=>',member)

from enum import Enum
# 将Student的gender属性改用枚举类型，可以避免使用字符串
class Gender(Enum):
    Male = '男'
    Female = '女'

class Student(object):
    def __init__(self,gender):
        self._gender = gender
    
huixiong = Student(Gender.Male)
print(huixiong._gender.value)


#----------------
# 使用元类

class Hello(object):
    def hello(self):
        print("test")

h = Hello()
print(type(h),type(Hello))
# type()函数可以查看一个类型或变量的类型。
# Hello 是一个类，他的类型是type
# h是一个实例，他 的类型就是class Hello

# 本质上，一个class就是通过type()创建出来的，所以我们可以使用type()直接创建出class

def fn(self,name='Wrold'):
    print('Hello,%s'% name)

Hello = type('Hello',(object,),dict(hello=fn))# 创建Hello class

h = Hello() # 创建一个Hello类的实例
h.hello() # 调用方法

# metaclass，元类。
# 如果想要创建出A类，要先根据metaclass创建出A类，再创建A类的实例.可以把metaclass看成是类的模板

# 例子:使用metaclas给自定义的MyList创建一个add方法
class ListMetaclass(type):# 习惯上metaclass类的类名这样写。斌且继承type
    def __new__(cls,name,bases,attrs):# 类对象，类名，父类集合，类的方法集合
        # 这个匿名方法就是调用当前对象的方法，并将结果放入attrs中，作为add的值
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

# 有了ListMetaclass后，就可以以他为模板创建类了，以后用这个MyList创建实例的时候就是用过，ListMetaclass的__new__方法创建实例
class MyList(list,metaclass=ListMetaclass):
    pass

# python解释器在创建类的时候会通过ListMetaclass中__new__方法创建。
# 所以就可以对创建类的时候做一些事儿，比如 增加新方法。
# 上面定义了add类。

L = MyList()
L.add(1)
print(L)

# 这里是一个使用Metaclass实现ORM的案例。https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072

class User(Model):
    id = IntegerField('id')
    name = StringField('username')

u = User(id=12345,name='huixiong')

u.save() #要实现这个功能。即创建一个这样的类，继承Model后就能自带save功能

#-----------------

class Field(object):
    def __init__(self,name,column_type):
        self.name = name # 字段名
        self.column_type = column_type # 字段类型

    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)

# 进一步定义子类
class StringField(Field):
    def __init__(self,name):
        super().__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name,'bigint')

# 定义元类
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':# 如果类名是Model的话，就创建一个
            print('Model __new__')
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s'% name)# 打印找到这个类的类名
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):# 如果方法是Field的的方法实例的话
                mappings[k] =v  # 将方法实例放到mappings中
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        print('%s __new__ '%name)
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    
    def __init__(self,**kwargs):
        print('Model __init__')
        super(Model, self).__init__(**kwargs)
    
    def __getattr__(self,key):
        try:
            return self[key] # 如果没有这个属性，抛出异常
        except KeyError:
            raise AttributeError(r"'Model' object has noattribute '%s'" % key)
    
    def __setattr__(self,key,value):
        self[key] = value

    def save(self):
        fields = [] # 字段
        params = [] # 参数
        args = [] # 变量
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s(%s) values(%s)'%(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s'% sql)
        print('ARGS:%s'% str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    def __init__(self, **kwargs):
        print('User __init__')
        super().__init__(**kwargs)

u = User(id='1',name='huixiong',email='example@email.com',password='123456')
print(isinstance(u,dict))
print(u.id)
u.save()
###
# python解释器
# 当用户定义User类时，python会在User中找定义的metaclass，如果没有就找父类的metaclass，如果都没有
# 最终会找到object(应该是的)。ModelMetaclass中做了几件事
# 1.排除对Model类的修改，
# 2.在当前类中查找定义的类的所有属性。如果找到就把他保存到mappings的dict中，同时从类中删除Field属性。不然容易出现运行时错误(实例的属性会覆盖同名的类的属性)。
# 3. 将表名保存到__table__中，这里的表名默认为类名。
# ###