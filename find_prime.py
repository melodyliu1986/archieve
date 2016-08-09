__author__ = 'liusong'


def isprime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            continue
    return True

print [i for i in range(1, 101) if isprime(i)]

