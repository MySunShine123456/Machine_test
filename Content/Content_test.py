#list数组
li=[1,2,3,'456',[1,2,3],{1:'one',2:'two'}]
print(type(list))
print(type(li))
#list元素访问
print('list元素访问')
print(li[0])
print(li[-1])
print(li[len(li)-1])
#查找元素位置
print('查找元素位置')
print(li.index('456'))
#添加元素
print('添加元素')
l_a=[1,2,3]
l_a.append([5,6,7])#append把[5,6,7]当做一个整体加入原来数组中
l_b=[7,8,9]
l_a.extend(l_b)#使用extend当做一个个元素加入到原来集合中
print(l_a)
#从数组里面删除元素
print('&&&&&&&&&&&&&&&&&&&&&&')
del(l_a[1])
print(l_a)
#判断是否为空使用not xx
l_a=[]
if not l_a:#not XX和 xx is None不是一回事
    print('empty')
#遍历数组
for i in li:#推荐使用
    print(i)
for i in range(len(li)):#根据索引访问元素
    print(li[i])
#字典，字典的顺序是随机的
d={'a':1,'b':2,1:'one',2:'two'}
print(type(d))
print(d)
#访问字典元素
print(d['a'])
#判断元素是否存在即判断key是否存在
print(5 in d)
#遍历字典元素
for key in d:
    print(d[key],end="")
for key ,value in d.items():
    print(key,value)
#set集合，本身无重复元素,set无索引

