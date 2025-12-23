import numpy as np
from numpy import array

myArray = np.array([2,3,4,56,7,4,7,8,9,5,4,5,7,7,5,4,3,3,5,23])

# search_value = np.where(myArray == 5)
# print(search_value)

def find_number(nums: array, target: int) -> int:
    for i in range(len(myArray)):
        if nums[i] == target:
            print(nums[i])

find_number(nums=myArray, target=23)
