class Position:
    def __init__(self, x, y, arrow, maxX, maxY):
        self.x = x
        self.y = y
        self.arrow = arrow  # RDLU - 0123
        self.maxX = maxX
        self.maxY = maxY

    def step(self, arrow):
        if arrow == 0:
            self.x = self.x + 1 if self.x < self.maxX - 1 else 0
        elif arrow == 1:
            self.y = self.y + 1 if self.y < self.maxY - 1 else 0
        elif arrow == 2:
            self.x = self.x - 1 if self.x > 0 else self.maxX - 1
        elif arrow == 3:
            self.y = self.y - 1 if self.y > 0 else self.maxY - 1

    def setArrow(self, val, prev):

        if val == 'S':
            self.arrow = prev
        elif val == 'R':
            self.arrow = self.arrow + 1 if self.arrow < 3 else 0
        elif val == 'L':
            self.arrow = self.arrow - 1 if self.arrow > 0 else 3

    def __str__(self):
        return f"{self.y}, {self.x}, {self.arrow}"


def solution(grid):
    answer = []
    visited = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    grid = [[c for c in row] for row in grid]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for a in [0,1,2,3]:
                cur = Position(x, y, a, len(grid[0]), len(grid))

                cnt = 0
                while not visited[cur.y][cur.x][cur.arrow]:
                    cnt += 1
                    # print(cur)

                    visited[cur.y][cur.x][cur.arrow] = 1
                    cur.step(cur.arrow)
                    cur.setArrow(grid[cur.y][cur.x], cur.arrow)

                if cnt:
                    answer.append(cnt)
    return sorted(answer)


print(solution(["SL", "LR"]))
