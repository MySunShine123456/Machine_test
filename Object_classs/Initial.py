#构造函数（给类赋值参数）
class Foo:
    def __init__(self,name1):#类在创建的时候是不能带参数的，你可以在构造函数的位置附加一些参数，这些参数是你在创建类时候的必要条件
        self.name=name1
    def hello(self,name):
        print('you are %s'%self.name)#self.name与构造函数的self.name对应
        print('I am %s'%name)
        print('\n')
obj=Foo('张三')
obj.hello('yh')