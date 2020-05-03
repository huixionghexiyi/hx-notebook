from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ['_name', '_hp']

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @property
    def alive(self):
        return self._hp > 0

    @classmethod
    def create_fighter(cls, name, hp):
        return cls(name, hp)

    @staticmethod
    def description(desc):
        return desc

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ['_name', '_hp', '_mp', 'set_address', '_address']

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(5, 15)

    def huge_attack(self, other):
        if self._mp >= 30:
            self._mp -= 30
            other.hp -= randint(25, 35)
            return True
        else:
            self.attack(other)
            return False

    def resume(self):
        incr_point = randint(5, 15)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '您的{}奥特曼\n生命值：{}\n魔法值：{}\n'.format(self._name, self._hp, self._mp)


class Monster(Fighter):
    slots = ['_name', '_hp']

    def attack(self, other):
        other._hp -= randint(10, 20)

    def __str__(self):
        return '您的{}怪兽\n生命值：{}'.format(self._name, self._hp)


def main():
    """ x 因为是抽象方法，本质上python没有提供抽象方法，这里继承ABCMeta来实现，@abstractmethod标注的方法为抽象方法"""
    # f = Fighter('huixiong',1000)
    """ x 使用classmethod修饰的方法创建Fighter也不行"""
    # f = Fighter.create_fighter('huixiong',1000)
    """ √ 可以使用其中的@staticmethod修饰的静态方法 """
    f = Fighter.description('This is a Abstract Class')
    """ """
    u = Ultraman('huixiong', 1000, 500)
    """ x 没有当前类中的 __clots__ 中添加 other ，所以不能附加属性 other """
    # u.other = 'not defind'
    """ 给实例 u 绑定方法"""
    from types import MethodType  # 引入方法类型
    def set_address(self, address): # 定义一个实例方法
        self._address = address
    u.set_address = MethodType(set_address, u) # 绑定方法
    u.set_address('china') # 调用方法
    print(u._address) # 获取值
    """  """
    print(type(u))
if __name__ == '__main__':
    main()
