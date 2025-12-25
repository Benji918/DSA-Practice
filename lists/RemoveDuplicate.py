def remove_duplicates(arr):
    unique_list = set(arr)
    return list(unique_list)



print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
# Output : [1, 2, 3, 4, 5]