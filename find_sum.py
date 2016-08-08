__author__ = 'liusong'


def find_sum(t_list, key):
    t_list = sorted(t_list)
    start = 0
    end = len(t_list) - 1
    while start < end:
        v_sum = t_list[start] + t_list[end]
        if v_sum > key:
            end -= 1
        elif v_sum < key:
            start += 1
        else:
            return t_list[start], t_list[end]
    return None

if __name__ == "__main__":
    # Find two item tha sum is 8.
    arrary = [4, 1, 2, 7, 11, 15]
    sum = 8
    result = find_sum(arrary, sum)
    if result is None:
        print "No value in the list."
    else:
        print "{0} + {1} = {2}".format(result[0], result[1], sum)

