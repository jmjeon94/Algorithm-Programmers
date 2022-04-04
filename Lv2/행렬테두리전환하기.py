def solution(rows, columns, queries):
    maps = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]

    answer = []
    for query in queries:
        ys, xs, ye, xe = query

        coords = []
        vals = []
        for dx in range(xs, xe):
            coords.append([ys, dx])
            vals.append(maps[ys - 1][dx - 1])
        for dy in range(ys, ye):
            coords.append([dy, xe])
            vals.append(maps[dy - 1][xe - 1])
        for dx in range(xs, xe)[::-1]:
            coords.append([ye, dx + 1])
            vals.append(maps[ye - 1][dx])
        for dy in range(ys, ye)[::-1]:
            coords.append([dy + 1, xs])
            vals.append(maps[dy][xs - 1])

        vals.insert(0, vals.pop())
        for v, (y, x) in zip(vals, coords):
            maps[y - 1][x - 1] = v

        answer.append(min(vals))

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
