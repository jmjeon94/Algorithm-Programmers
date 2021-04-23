from collections import defaultdict, deque
def solution(n, edge):
    distances = [0] * (n+1)
    visited = [0] * (n+1)

    # init
    edges = defaultdict(list)
    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])

    q = deque()
    q.append(1)
    visited[1] = 1

    # dfs
    while q:
        v = q.popleft()
        for w in edges[v]:
            if not visited[w]:
                q.append(w)
                distances[w] = distances[v] + 1
                visited[w] = 1

    return distances.count(max(distances))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))