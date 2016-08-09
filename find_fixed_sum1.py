__author__ = 'liusong'
import time

start_time = time.time()
t_list = [1, 4, 7, 2, 8, 9, 5, 6]
len_t_list = len(t_list)
for i in range(0, len_t_list-1):
    r_list = [1, 4, 7, 2, 8, 9, 5, 6]
    del r_list[i]
    print r_list
    for j in r_list:
        if t_list[i] + j == 10:
            print "{0} + {1} = 10".format(t_list[i], j)
end_time = time.time()
duration_time = end_time - start_time
print "Run time: {0}".format(duration_time)
