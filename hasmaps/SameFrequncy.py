
def check_same_frequency(list1, list2):
    return all(x == y for x,y in zip(list1, list2))



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)