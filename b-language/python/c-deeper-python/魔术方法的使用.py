'''
1. 学习基本语法
2. 学习魔术方法
3. 待续
'''
# Python魔术方法


class Student(object):

    '''
    基本魔术方法
    '''

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.value = [i for i in args]

    def __new__(cls, name, age,*args):
        return super().__new__(cls)

    def __del__(self):
        print("__del__ called")

    def __call__(self, name):
        '''
        当实例对象被当作函数一样调用时
        '''
        print("__call__ called:%s" % name)

    def __len__(self):
        print("__len__ called")

    def __repr__(self):
        '''
        直接执行对象时，调用的方法
        '''
        print('__repr__ called')
        return super().__repr__()

    def __str__(self):
        print("__str__ called")
        return super().__str__()

    def __bytes__(self):
        print("__bytes__ called")

    def __hash__(self):
        print("__hash__ called")

    def __bool__(self):
        '''
        被bool()方法调用时，返回的结果
        '''
        print("__bool__ called")
        return True

    def __format__(self, format_desc):
        print("__format__ called")

    '''
    有关属性
    '''

    def __getattr__(self, name):
        '''
        调用了一个，找不到属性时的时候才会调用该方法
        '''
        print('__getattr__ called:%s'%name)

    def __setattr__(self, name, value):
        '''
        设置一个属性时执行的方法
        设置属性，无需有返回值
        '''
        print('__setattr__ called:%s'%name)
        # self.__dict__[name] = value # 这种方式也可以设置，不推荐
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print('__delattr__ called')
        return super().__delattr__(name)

    def __getattribute__(self, name):
        '''
        每次访问一个属性都会调用，不推荐使用，使用__getattr__ 就好了
        '''
        print('__getattribute__ called:%s'%name)
        return super().__getattribute__(name)

    '''
    property
    当该类的实例，被作为属性赋值给另一个类的实例时调用的方法
    '''

    def __set__(self, instance, value):
        '''
        被作为属性设置时，value：该属性属于哪个类
        '''
        print('__set__', 'instance:', instance, 'owner:', value)

    def __get__(self, instance, owner):
        '''
        被作为属性被调用时，owner：该属性属于哪个类
        '''
        print('__get__', 'instance:', instance, 'owner:', owner)

    def __delete__(self, instance):
        '''
        被作为属性被删除时，instance：该实例对象
        '''
        print('__delete__', 'instance:', instance)

    '''
    运算符相关方法
    '''

    def __add__(self, other):
        '''
        当执行加法运算时
        '''
        print('__add called')
        return other - 1

    def __radd__(self, other):
        '''
        当左边的对象没有 __add__ 方法时
        '''
        print('__radd__ called,left object not have __add__')
        return 0

    '''
    容器类相关：dict/tuple/list 等
    '''

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, val):
        self.value[key] = val

    def __delitem(self, key):
        del self.value[key]


class Socialer():
    occupation = Student('huixiong', 19)

    def __init__(self):
        super().__init__()


a = Student('huixiong', '17','a','b','c','d')
a('huixiong')
bool(a)
m = a.gender
a.sex = 'man'
del a.sex # 报错，因为没有gender属性
b = Socialer()
b.occupation
b.occupation = a # 这里回调用__repr__,因为a对象呗直接调用，赋值给了b
del b.occupation
print(a+1)
print(b+a)
print(a[1])
print(a[3])
del a[3]
print(a[3])