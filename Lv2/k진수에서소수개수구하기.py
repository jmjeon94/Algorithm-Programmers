def isPrime(n):
    if n<=1: return False
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
           return False
    else:
        return True
def solution(n, k):

    changed = ''
    while n:
        changed = str(n%k) + changed
        n = n//k

    answer = 0
    for num in changed.split('0'):
        if num and isPrime(int(num)):
            answer+=1

    return answer
print(solution(2, 3))