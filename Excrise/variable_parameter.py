#支持可变参数的函数
def testFun1(**arg):
    for k in arg.keys():
        print("arg[%s] = %s."%(k, arg[k]))
def testFun2(*arg1, **arg2):
    print(arg1,arg2)
if __name__ == '__main__':
    print("How do you do? %d, %d", 2, 3)
    testFun1(One=1, Two=2)
    testFun2(1, 2, 3, One=1, Two=2, Three=3)