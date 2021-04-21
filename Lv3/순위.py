from collections import defaultdict

def dfs(cur, v, n, edges, mat, visited):

    for w in edges[v]:
        if not visited[w]:
            mat[v][w] = 1
            mat[w][v] = -1
            mat[cur][w] = 1
            mat[w][cur] = -1
            visited[w] = 1

            dfs(cur, w, n ,edges, mat, visited)

def solution(n, results):
    edges = defaultdict(list)
    mat = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for a, b in results:
        edges[a].append(b)

    for v in range(1, n+1):
        visited = [0] * (n+1)
        dfs(v, v, n, edges, mat, visited)

    answer = 0
    for m in mat:
        print(m)
        answer += m.count(0)==2
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

