from itertools import combinations

def solution(line):

    comb = list(combinations(line, 2))
    xs, ys = [], []

    for m, n in comb:
        a, b, e = m
        c, d, f = n

        norm = a*d - b*c
        if norm:
            x = ((b*f - e*d) / norm)
            y = ((e*c - a*f) / norm)

            if x==int(x) and y==int(y):
                xs.append(x)
                ys.append(y)
    xmax, xmin = max(xs), min(xs)
    ymax, ymin = max(ys), min(ys)
    xs = list(map(lambda x: x-xmin, xs))
    ys = list(map(lambda y: -y, ys))
    ys = list(map(lambda y: y+ymax, ys))

    stars = [['.' for __ in range(int(xmax-xmin+1))] for _ in range(int(ymax-ymin+1))]
    for y, x in zip(ys, xs):
        stars[int(y)][int(x)] = '*'

    answer = []
    for r in stars:
        answer.append(''.join(r))

    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
