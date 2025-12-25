
def first_second(my_list):
    max_val = max(my_list)

    second_max_value = max([i for i in my_list if i < max_val])

    return max_val, second_max_value




myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87