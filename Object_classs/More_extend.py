#经典类的时候，就按照深度优先方式查找继承的方法,
#新式类的时候，就按照广度优先的方式查找
class D(object):

    def bar(self):
        print('D.bar')
class C(D):

    def bar(self):
        print('C.bar')


class B(D):

    pass

class A(B, C):

    pass

a = A()
a.bar()