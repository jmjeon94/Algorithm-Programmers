from collections import defaultdict

paths = []
answer = []
visited = defaultdict(list)

def dfs(edges, cur, length):
    global answer

    paths.append(cur)

    if len(paths) == length+1 and not answer:
        answer = paths.copy()

    for i, w in enumerate(edges[cur]):
        if visited[cur][i] == 0:
            visited[cur][i] = 1
            dfs(edges, w, length)
            visited[cur][i] = 0

    paths.pop()

def solution(tickets):
    edges = defaultdict(list)
    for a, b in tickets:
        edges[a].append(b)

    for k in edges:
        edges[k].sort()
        visited[k] = [0]*len(edges[k])

    dfs(edges, 'ICN', len(tickets))

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))