__author__ = 'liusong'

test_list = [1, 9, 7, 6, 4, 3]
len_test_list = len(test_list)

for i in range(0, len_test_list):
    for j in range(len_test_list - 1 - i):
        if test_list[j] > test_list[j+1]:
            tmp = test_list[j]
            test_list[j] = test_list[j+1]
            test_list[j+1] = tmp
print test_list


