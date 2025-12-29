def traverse_dic(dic):
    for i, v in enumerate(dic):
        print(i,v)

test_dic = {'one': 1, 'two': 2}
# traverse_dic(test_dic)

# print(test_dic.get('one'))
# print(test_dic.keys())
# print(test_dic.items())
# # print(test_dic.pop('two')
# test_dic.update({'v':23, '3': 'name'})
# print(len(test_dic))
for k , v in enumerate(test_dic):
    print(k,v)