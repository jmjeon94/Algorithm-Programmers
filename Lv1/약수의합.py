def solution(n):
    return sum([x for x in range(1,n//2+1) if n%x==0])+n

print(solution(12))