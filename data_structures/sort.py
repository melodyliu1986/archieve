# This is bubble sort program.

test = [6, 5, 3, 4, 2, 1]


def bubble_sort(test_list):
    len_test_list = len(test_list)
    for i in range(len_test_list-1, 0, -1):
        print "*"*20
        print i
        for j in range(i):
            if test_list[j] > test_list[j + 1]:
                tmp = test_list[j+1]
                test_list[j+1] = test_list[j]
                test_list[j] = tmp
    return test_list

print test
print bubble_sort(test)

