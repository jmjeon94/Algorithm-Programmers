def solution(n, times):
    left = 1
    right = max(times) * n
    while left<right:
        middle = (left+right)//2

        if sum([middle//x for x in times]) >= n:
            right = middle
        else:
            left = middle+1

    return left

print(solution(6, [7, 10]))