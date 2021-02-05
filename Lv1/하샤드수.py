def solution(x):
    return x%sum([int(n) for n in str(x)])==0

print(solution(18))