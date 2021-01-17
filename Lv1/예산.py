def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution([2, 2, 3, 3], 10))