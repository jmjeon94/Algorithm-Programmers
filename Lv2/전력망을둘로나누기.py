# 전선의 연결을 하나씩 끊어보고, 두 개의 트리 중 하나에 대해서 트리의 노드개수를 구하면 차이값을 구할 수 있다.
cnt = 0
def dfs(map, visited, v):
    global cnt
    cnt+=1
    visited[v] = 1
    for w in range(1, len(map)):
        if not visited[w] and map[v][w]:
            dfs(map, visited, w)

def solution(n, wires):

    global cnt

    map = [[0] * (n+1) for _ in range(n+1)]

    for w in wires:
        map[w[0]][w[1]] = 1
        map[w[1]][w[0]] = 1

    min_diff = len(map)

    for w in wires:
        visited = [0] * (n + 1)
        cnt = 0
        map[w[0]][w[1]] = 0
        map[w[1]][w[0]] = 0
        dfs(map, visited, 1)
        map[w[0]][w[1]] = 1
        map[w[1]][w[0]] = 1
        min_diff = min(min_diff, abs(cnt - (len(map)-1-cnt)))

    return min_diff
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
