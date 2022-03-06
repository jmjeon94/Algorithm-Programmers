max_depth = 0

def dfs(k, visited, dungeons, cur_d, depth):
    global max_depth

    visited[cur_d] = 1
    max_depth = max(depth, max_depth)

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            dfs(k-dungeons[cur_d][1], visited, dungeons, i, depth + 1)

    visited[cur_d] = 0


def solution(k, dungeons):
    global max_depth

    visited = [0] * len(dungeons)

    for i in range(len(dungeons)):
        dfs(k, visited, dungeons, i, 1)

    return max_depth

print(solution(80, [[80,20],[50,40],[30,10]]))

