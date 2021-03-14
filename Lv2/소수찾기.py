from itertools import permutations


def isPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True

    root = int(num ** (1 / 2))
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    target_array = []

    array = [x for x in numbers]
    for i in range(1, len(array) + 1):
        _list = list(permutations(array, i))
        target_array += _list
    target_array = list(set([int(''.join(x)) for x in target_array]))

    for n in target_array:
        if isPrime(n):
            cnt += 1
    return cnt


solution('101')