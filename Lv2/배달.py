from collections import defaultdict
import sys

def solution(N, road, K):

    visited = [True, True] + [False] * (N-1)
    distance = [0, 0] + [sys.maxsize] * (N-1)

    graph = defaultdict(list)
    graph[1].append([1, 0])
    for r in road:
        graph[r[0]].append([r[1],r[2]])
        graph[r[1]].append([r[0],r[2]])

    while sum(visited)<N+1:

        min_ = sys.maxsize
        v = 1
        for i in range(1, N+1):
            if not visited[i]:
                if distance[i] < min_:
                    min_ = distance[i]
                    v = i

        for w in graph[v]:
            if not visited[w[0]]:
                if distance[w[0]] > distance[v]+w[1]:
                    distance[w[0]] = distance[v]+w[1]

        visited[v] = True

    answer = len(list(filter(lambda x: x<=K, distance)))-1
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))