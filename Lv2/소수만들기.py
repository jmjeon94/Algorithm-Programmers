from itertools import combinations

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for selected in comb:
        if isPrime(sum(selected)):
            answer+=1

    return answer

print(solution([1,2,7,6,4]))