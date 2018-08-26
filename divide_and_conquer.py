def quicksort(array):
    if len(array) < 2 :
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        # 书上没有'='，个人认为如果有相等的数，先放入一边，再排序,这样增加了排序次数但是简化了代码，也可单独增加条件处理相等的数
        greater = [i for i in array[1:] if i >= pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([17, 8, 8, 35, 82, 2]))