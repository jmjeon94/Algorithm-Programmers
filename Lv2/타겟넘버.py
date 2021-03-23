answer=0
def dfs(idx, numbers, target, value):
    global answer

    if value==target and idx==len(numbers):
        answer+=1
        return
    if idx==len(numbers):
        return

    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])


def solution(numbers, target):
    global answer

    dfs(0, numbers, target, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
