def max_product(arr):
    # TODO: Find the biggest 2 numbers in the array/list
    max_arr_value = max(arr)
    print(max_arr_value)
    second_max_value = max([i for i in arr if i < max_arr_value ])
    print(second_max_value)

    # TODO: Perform the product of the 2 largest numbers
    return max_arr_value * int(second_max_value)


arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr)) # Output: 63 (9*7)