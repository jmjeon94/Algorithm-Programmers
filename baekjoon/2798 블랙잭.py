# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
n, m = 10, 500
nums = list(map(int, '93 181 245 214 315 36 185 138 216 295'.split()))

visited = [0] * len(nums)
max_ = 0

def dfs(cur, accum, depth):
    global max_
    if depth == 3:
        max_ = max(accum, max_)
        return

    visited[cur] = 1
    for next in range(len(nums)):
        if not visited[next] and accum + nums[next] <= m and cur < next:
            dfs(next, accum + nums[next], depth + 1)
    visited[cur] = 0


for i in range(len(nums)):
    dfs(i, nums[i], 1)

print(max_)
# max(filter(lambda x:x<=m, map(sum, combinations(nums, 3))))