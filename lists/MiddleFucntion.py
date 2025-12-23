def middle(arr):
    arr.pop(0)
    del arr[-1]
    return arr



myList = [1, 2, 3, 4]
middle(arr=myList)  # [2,3]