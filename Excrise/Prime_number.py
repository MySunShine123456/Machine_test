#打印100以内的素数
def prime(numbers):
    for i in range(1,numbers+1):
        flag = True
        if i>1:
            for j in range(2,i):
                if ( i % j == 0):
                    flag=False
                    break
            if flag:
                print(i,' ',end="")
prime(10)
