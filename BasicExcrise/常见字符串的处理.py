#分割与合并字符串
import  string
#1)去除空格的操作
s=" abcd efg "
print(s.strip())
print(s.lstrip())#删除左边的空格
print(s.rstrip())#删除右边的字符串
print(s)
#字符串的连接
s="abc def"
print(s.upper())#全部转化为大写
print(s.upper().lower())#全部转化为小写
print(s.capitalize())#首字母转化为大写
#位置比较
s_1='abcdefg'
s_2='abdeffxx'
print(s_1.index('bcd'))
try:
    print(s_2.index('bcd'))
except ValueError:
    print('Valueerror')
#长度
print(len(''))
s=''
if s is None:
    print('None')
else:
    print('empty')#空字符串和false(not s)等价
#字符串的分割和连接
s='abc,,def,,ghi'
splitted=s.split(',')
print(type(splitted))
print(splitted)
#按行分割
s="""abc
def
ghi
mnl"""
s_1=s.split('\n')
print(s_1)
s_2=s.splitlines()
print(s_2)
s=['abc','def','ghi']
print('-'.join(s))
#字符串转化为数组
s='abcdefg'
s=list(s)
print(s)
print('字符串按单词反转')
#字符串按单词反转（必须包含所有空格）
def reserve(str_list, start, end):
    while start <= end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        end -= 1
        start += 1
str = ' I love china!'
str_list = list(str)#将字符串转为数组
print(str_list)
i = 0
print(len(str_list))

# 从前往后遍历list，如果碰到空格，就调用反转函数，不考虑单个字符情况
while i < len(str_list):
    if str_list[i] != ' ':
        start = i
        end = start + 1
        print(end)
        while (end < len(str_list)) and (str_list[end] != ' '):
            end += 1
        if end - start > 1:
            reserve(str_list, start, end - 1)
            i = end
        else:
            i = end
    else:
        i += 1

print(str_list)
str_list.reverse()
print(''.join(str_list))
#
# # 采用正则表达式操作
# str_re = re.split(r'(\s+)', str)
#
# str_re.reverse()
# str_re = ''.join(str_re)
# print(str_re)
#None的使用
x=None
if  not x:
    print('None')
else:
    print('Not None')
#continue pass break用法，return直接跳出函数
for i in range(0,100):
    if i<10:
        pass
    elif i<30:
        continue#
    elif i<35:
        print(i)
    else:
        break
#函数
def fun(a,b):
    print(a,b)
    return (a+b)
c=fun(10,20)
print(type(c))
print(c)
#可变参数
def func(name,*numbers):#*表示将参数放到一个数组里面,两个*表示将参数放入字典中，可变参数必须在最后
    print(numbers)
    print (type(numbers))
func('Tom',1,2,3,4,'abc')#元组是只可读的list
print('+++++++++++++')
#*后面的变量传递参数的时候一定要把名字带上
def func1(a,b,c,*,china,uk):
    print(china,uk)
func1(2,1,3,china='BJ',uk='LD')
#可变参数既有字典也有默认参数
print('***************************')
def func(a,b,c=0,*args,**kvs):
    print(a,b,c)
    print(args)
    print(kvs)
func(1,2)
func(1,2,3)
func(1,2,3,'a','b','c')
func(1,2,3,*('a','b'),**{'china':'BJ','uk':'LD'})
#*参数前面有*表示可变参数
#递归
def fib(n):
    if n<1:
        raise ValueError
    elif n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)#与n范围结构一致，这是缩小了范围
print(fib(10))
#hanoi问题
def hanoi(n,source,target,helper):
    if n==1:
        print(source+'->'+target)
    else:
        hanoi(n-1,source,helper,target)
        print(source+'->'+target)
        hanoi(n-1,helper,target,source)
hanoi(4,'A','B','C')
#函数是可以作为参数的
p=print
p(1,2,4)
def sum(x,y,p=None):
    s=x+y
    if p:
        p(s)
    return s
sum(100,200)
sum(100,300,print)
def cmp(x,y,cp=None):
    if not cp:
        if x>y:
            return 1
        elif x<y:
            return -1
        else:
            return 0
    else:
        return cp(x,y)
def my_cp(x,y):#指定的比较函数
    if x<y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
print(cmp(100,200))
print(cmp(100,200,my_cp))