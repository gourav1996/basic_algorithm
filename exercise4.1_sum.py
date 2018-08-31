def sum(li):
    if li == []:
        return 0
    return li[0] + sum(li[1:])

if __name__ == "__main__":
    print(sum([1, 3, 5, 7, 9, 11]))