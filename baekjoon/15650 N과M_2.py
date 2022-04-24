n, m = 4, 2

visited = [0] * (n+1)

def dfs(v, depth):
    visited[v] = 1

    if depth==m-1:
        return

    for w in range(1, n+1):
        if not visited[w]:
            dfs(w, depth+1)

    visited[v] = 0


for i in range(1, n+1):
    dfs(i, depth=0)