__author__ = 'liusong'


def reverse_string1(t_str):
    t_str = list(t_str)
    start_index = 0
    end_index = len(t_str) - 1
    while start_index < end_index:
        tmp = t_str[start_index]
        t_str[start_index] = t_str[end_index]
        t_str[end_index] = tmp
        start_index += 1
        end_index -= 1
    return ''.join(t_str)


def reverse_string2(t_str):
    t_str = list(t_str)
    len_t_str = len(t_str)
    l_str = range(0, len_t_str)
    j = len_t_str - 1
    for i in t_str:
        l_str[j] = i
        j -= 1
    return ''.join(l_str)


def reverse_string3(t_str):
    return t_str[::-1]


def reverse_string4(t_str):
    t_str = list(t_str)
    t_str.reverse()
    return ''.join(t_str)

if __name__ == "__main__":
    l = "abcdefg"
    print reverse_string1(l)
    print reverse_string2(l)
    print reverse_string3(l)
    print reverse_string4(l)
