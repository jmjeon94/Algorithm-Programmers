def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))

print(solution(3, 3))
