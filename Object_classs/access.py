#举个学生的例子，我们可以用一个学生类来存储学生的信息，但是我们在外部可以接触到name，那么其实我们就是可以直接修改name的，这是不安全的
class Student:
    def __init__(self,name,age):
        self.name=name#self.name可以使name变成全局变量,若想变量变成私有的则定义为self__name=name外界就不能修改了
        self.age=age
    def detail(self):
        print(self.name)#自我调用
        print(self.age)
LiLei=Student('张三',20)
LiLei.age=19
LiLei.detail()
