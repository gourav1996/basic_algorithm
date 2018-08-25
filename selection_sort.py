"""选择排序将数组按从大到小或从小到大的排列，思路是：
1. 找出A数组中最大（小）的数，将其拿出放入B数组中
2. 重复1步骤，直至A数组的数全部取出放入B数组中
以下代码按照从小到大的顺序排列"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[1]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr
print(selectionSort([4, 83, 13, 8, 9, 17]))