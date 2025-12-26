# Product and Sum of array elements
import math
def product_sum(array):
    summation = sum(array)
    product_array = math.prod(array)
    return summation, product_array


print(product_sum([1,6]))
