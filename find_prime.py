__author__ = 'liusong'


def isprime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            continue
    return True

# Get all the prime between 1 and 100.

print [i for i in range(1, 101) if isprime(i)]
