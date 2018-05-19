#在数组里面返回两个索引值，若两个值得和是target
def two_sum(numbers,target):#输入和输出
    for i in range(len(numbers)-1):#len(numbers)-1的目的是使最后一个元素留给j
        for j in range (i+1,len(numbers)):
            if(numbers[i]+numbers[j])==target:
                return i,j
    return -1,-1#找不到时返回-1
print(two_sum([2,7,11,15],17))
print(two_sum([2,7,11,18],30))