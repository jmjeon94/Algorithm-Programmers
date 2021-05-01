from collections import deque
arrows = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우

def solution(maps):

    r, c = len(maps), len(maps[0])
    depth_map = [[-1 for _ in range(c)] for _ in range(r)]
    depth_map[0][0] = 1

    q = deque([(0,0)])
    while q:
        y, x = q.popleft()
        if y==r-1 and x==c-1:
            return depth_map[y][x]
        for arrow in arrows:
            new_y = y + arrow[0]
            new_x = x + arrow[1]
            if -1 < new_y < r and -1 < new_x < c and maps[new_y][new_x]==1:
                if depth_map[new_y][new_x] == -1:
                    depth_map[new_y][new_x] = depth_map[y][x] + 1
                    q.append((new_y,new_x))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

arr2d = [[0] * 3 for _ in range(4)]
arr2d = [[0]*3] * 4
arr2d = [[0 for _ in range(3)] for _ in range(4)]
arr2d[0][0]=1
arr2d