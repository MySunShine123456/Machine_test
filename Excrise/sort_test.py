#实现一个sort,通过指定的排序函数用来实现按不同顺序进行排序
# 冒泡排序法实现升序排列
def bubble_sort(lists, sort=None):
    if not sort:
        count = len(lists)
        for i in range(0, count):
            for j in range(i + 1, count):
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
        return lists
    else:
        return sort(lists)
# 直接选择排序法实现降序排列
def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        max = i
        for j in range(i + 1, count):
            if lists[max] < lists[j]:
                max = j
        lists[max], lists[i] = lists[i], lists[max]
    return lists
# 输入数据测试
s = [1, 5, 3, 9, 7, 13, 78, 54, 43, 32, 1, 4, 10]
print(s)
print('bubble_sort= %s' % bubble_sort(s))
print('select_sort= %s' % bubble_sort(s, sort=select_sort))