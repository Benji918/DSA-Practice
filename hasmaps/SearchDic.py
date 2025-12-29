def search_dic(dic, value):
    for key in dic:
        if dic[key] == value:
          return key, value
    return 'Value no exist!!!!'



test_dic = {'one': 1, 'two': 2}
print(search_dic(test_dic, 2))