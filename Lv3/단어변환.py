import sys
min_ = sys.maxsize
def check_dup(a, b):
    cnt = 0
    for x, y in zip(a,b):
        if x==y: cnt+=1
    return cnt==len(a)-1

def dfs(cur, target, v, visited, words, depth):
    global min_

    if cur==target:
        min_ = min(min_, depth)
        return min_

    for i, word in enumerate(words):
        if visited[i]==0 and check_dup(cur, words[i]):
            visited[i] = 1
            dfs(words[i], target, i, visited, words, depth+1)
            visited[i] = 0

def solution(begin, target, words):

    if not target in words:
        return 0

    visited = [0] * len(words)
    dfs(begin, target, 0, visited, words, 0)

    return min_

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))