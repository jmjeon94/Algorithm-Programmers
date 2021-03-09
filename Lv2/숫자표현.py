def solution(n):
    answer = 0
    l , r = 0, 0
    while l<n or r<n:
        tmp = r*(r+1)//2 - l*(l+1)//2
        if tmp>n:
            l+=1
        elif tmp<n:
            r+=1
        else:
            answer += 1
            l, r = l+1, r+1
        print(l, r)
    return answer

print(solution(15))