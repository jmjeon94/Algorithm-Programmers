def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        r, c = i // n, i % n
        answer.append(max(r+1,c+1))
    return answer

print(solution(2,3,3))