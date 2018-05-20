# 创建类,类中的函数第一个参数必须是self，类中定义的函数叫做“方法”。
class Foo:
    # 这里我们可以创建一个类级别的变量
    # 它不会随着由此类创建的变量而变化
    name = 'Jan'
    def bar(self):
        print('Bar')
    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')
# 根据Foo创建的对象
obj1 = Foo()
obj2 = Foo()
obj1.hello('August')
obj2.hello('July')