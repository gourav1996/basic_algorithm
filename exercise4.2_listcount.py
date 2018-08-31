def list_count(arr):
    if arr == []:
        return 0 
    return 1 + list_count(arr[1:])

if __name__ == "__main__":
    print(list_count(range(9)))