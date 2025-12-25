import numpy as np

pair_values = []

def pair_sum(array, target):
    for i in range(len(array)):
        for g in range(i+1, len(array)):
            if array[i] == array[g]:
                continue
            elif array[i] + array[g] == target:
                new_pair = str(array[i]) + "+" + str(array[g])
                pair_values.append(new_pair)

    return pair_values


arr = np.array([2, 4, 3, 5, 6, -2, 4, 7, 8, 9])
print(pair_sum(arr, 7))