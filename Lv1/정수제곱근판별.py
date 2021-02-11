def solution(n):
    return int((n**(1/2)+1)**2 if n==int(n**(1/2))**2 else -1)

print(solution(121))