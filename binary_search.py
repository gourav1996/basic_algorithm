def binary_search(lists, item):
    """二分法查找目标数字"""
    low = 0 
    high = len(lists) -1
    if low <= high: # 如果范围没有缩小到只包含一个元素，继续缩小范围
        mid = (low + high)/2
        guess = lists[mid]
        if guess == item:
            return mid
        if guess > item:
            low = mid - 1 
        else:
            high = mid + 1
    return None

mylist = [1, 3, 5, 7, 9]
binary_search(mylist, 5)
