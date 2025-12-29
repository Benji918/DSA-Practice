def merge_dicts(dict1, dict2):
    ''' Merge two dictionaries '''
    new_dic = {}

    for k in dict1.keys() | dict2.keys():
        v1 = dict1.get(k,0)
        v2 = dict2.get(k,0)
        new_dic[k] = v1 + v2

    return new_dic





dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))