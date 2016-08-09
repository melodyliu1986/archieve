__author__ = 'liusong'

import time

start_time = time.time()
t_list = [1, 4, 7, 2, 8, 9, 5, 6]

t_list = sorted(t_list)
start_index = 0
end_index = len(t_list) - 1
while start_index < end_index:
    if t_list[start_index] + t_list[end_index] < 10:
        start_index += 1
    elif t_list[start_index] + t_list[end_index] > 10:
        end_index -= 1
    else:
        print "{0} + {1} = {2}".format(t_list[start_index], t_list[end_index], 10)
        start_index += 1
        end_index -= 1
        continue

end_time = time.time()
print "Time: {0}".format(end_time - start_time)
