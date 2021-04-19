from functools import reduce
from math import gcd

def solution(arr):
    return reduce(lambda x, y: x*y//gcd(x, y), arr)

print(solution([2,6,8,14]))