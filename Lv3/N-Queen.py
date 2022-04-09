answer = 0
map = []
def dfs(row, col, n):
    global answer
    global map
    map[row] = col

    if row==n:
        answer += 1

    for col2 in range(1, n+1):
        if col2 in map:
            continue
        for ref in range(1, row+1):
            if abs(ref-(row+1))==abs(map[ref]-col2):
                break
        else:
            dfs(row+1, col2, n)

    map[row] = 0

def solution(n):
    global map
    global answer

    for col in range(1, n+1):
        map = [0] * (n+1)
        dfs(1, col, n)
    return answer

print(solution(4)) # 2