answer = [1] * 5

def dfs(place, i, j, depth, visited, pth):

    visited[i][j] = 1

    if place[i][j]=='P' and depth>0:
        answer[pth] = 0
        return

    if depth>1:
        return

    for y, x in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if i+y>4 or i+y<0 or j+x>4 or j+x<0:
            continue
        if not place[i+y][j+x]=='X' and not visited[i+y][j+x]:
            dfs(place, i+y, j+x, depth+1, visited, pth)

    visited[i][j] = 0

def solution(places):
    for n, place in enumerate(places):
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    visited = [[0] * 5 for _ in range(5)]
                    dfs(place, i, j, 0, visited, n)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

