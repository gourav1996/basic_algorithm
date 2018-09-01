def binary_search(low, high, aim):
    mid = (low + high) // 2
    if low > high:
        return -1
    if arr[mid] == aim:
        return mid
    elif arr[mid] > aim:
        return binary_search(low , mid + 1, aim)
    else:
        return binary_search(mid - 1 , high, aim)

if __name__ == "__main__":
    arr = range(20)
    low = 0 
    high = len(arr) - 1
    aim = 7
    search_index = binary_search(low, high, aim)
    if search_index == -1 :
        print("不含有元素：%d"%aim)
    else:
        print("含有该元素，该元素的索引为:%d" %search_index)