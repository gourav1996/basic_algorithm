def find_max_by_recursion(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max_by_recursion(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

def findmax_by_loop(arr):
    maxfigure = arr[0]
    for i in arr[1:]:
        if maxfigure < i:
            maxfigure = i
    return maxfigure

if __name__ == "__main__":
    print(find_max_by_recursion(range(9)))
    print(findmax_by_loop(range(9)))