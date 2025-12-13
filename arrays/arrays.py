import array

my_array = array.array('i')
array1 = array.array('i', [1,2,3,4,5])
arr2 = array1.insert(8, 23)

test_arr = array.array('i', [1,2,3,4,5,5])
test_arr.append(4)

test_arr2 = array.array('i', [1,2,3,4,5,5])
test_arr2.extend({5,5,5})
print(test_arr2)
print(test_arr2.count(5))

print(test_arr2.tobytes())


print(test_arr2[:3])