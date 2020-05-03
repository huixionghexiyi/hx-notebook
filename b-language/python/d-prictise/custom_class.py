"""
定制类
"""
# __str__
# __repr__
# __iter__
# __next__
# __getitem__
# __len__
# __getattr__
# __call__


class Person(object):
    """ 
    Person类
    """

    def __init__(self, name='none',  hair_num=0):
        """ 
        创建实例的时候调用的方法 
        创建内部属性 _name,_hair_num
        """
        self._name = name
        self._hair_num = hair_num

    def __str__(self):
        """
        在print(p) 时可以输出内容，而不是类属性
        """
        return self._name

    def __repr__(self):
        ''' 
        在控制台输出Person的实例对象的时候
        输出内容
        '''
        return self._name

    def __iter__(self):
        '''
        实现该方法，才能使用for ... in 迭代
        '''
        return self

    def __next__(self):
        """
        迭代对象中 for ... in ...
        每次循环元素都是调用 __next__ 方法
        """
        if self._hair_num < 10:
            self._hair_num += 1
            return self._hair_num
        else:
            raise StopIteration()

    def __getitem__(self, n):
        '''
        若想使用索引查找:
        p = Person("huixiong")
        p[0]
        若想使用切片:
        p[0:2]
        需要加判断
        '''

        if isinstance(n, int):
            return n
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            L = [i for i in range(n.stop)]
        return L

    def __getattr__(self, attr):
        '''
        当调用对象不存在的属性时，这个方法会被执行,attr为调用的属性名。
        '''
        if attr == 'nose':
            return 'i have no nose.'
        elif attr == 'other':
            return lambda attr: 'i dont have %s either' % attr
        else:
            raise AttributeError()

    # def __call__(self, other):
    #     '''
    #     使实例对象可以直接进行 p()调用。
    #     '''
    #     return self._name+' '+other


def main():
    p = Person('huixiong')
    # print(p)
    # for x in p:
    #     print(x)
    # print(p[2])
    # print(p[0:3])
    # print(p.nose)
    # print(p.other('mouth')) #
    print(p('fuck'))  # 可以使用实例对象进行调用
    print(callable(Person()))  # 判断是否


if __name__ == '__main__':
    main()
