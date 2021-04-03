def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a
    while n>=2:
        if a%2==1 and a+1==b:
            break
        a = (a+1)//2
        b = (b+1)//2
        n /= 2
        answer+=1
    return answer

print(solution(8, 4, 7)) # 3