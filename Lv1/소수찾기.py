def solution(n):
    answer = [1] * (n+1)
    for i in range(2, int(n**(1/2))+1):
        j = 2
        while j*i <= n:
            answer[j*i] = 0
            j+=1

    del answer[0]
    return sum(answer)-1 # 1은 제외

print(solution(5))


