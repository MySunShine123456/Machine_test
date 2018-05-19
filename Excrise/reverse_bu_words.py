#字符串反转(先把单词反转再将字符串反转)
def reverse(str_list,start,end):
    while start<end:
        str_list[start],str_list[end]=str_list[end],str_list[start]#python中快速交换两个值得写法
        start+=1
        end-=1
stence=' Hello, how are you? Fine.  '
#使用大量的数据遍历时使用数组，当想要快速遍历时使用map
str_list=list(stence)#由于字符串不能修改，所以将字符串转化为数组
i=0
while i<len(str_list):
    #13-19行是单词从开始到结束的位置对整个单词进行反转
    if str_list[i]!=' ':#如果list集合不为空格
        start=i
        end=start+1
        # end一直从start+1的开始的位置开始读，读到一个单词的长度即遇到空格
        while(end<len(str_list))and(str_list[end] !=' '):
                end+=1
        reverse(str_list,start,end-1)#否则对单词做反转
        i=end#下次循环的位置即从end位置继续朝前走
    else:
        i+=1
str_list.reverse()#将整个字符串进行反转
print(str_list)
#将list转化为字符串
print(''.join(str_list))






