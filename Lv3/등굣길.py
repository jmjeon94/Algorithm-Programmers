def solution(m, n, puddles):

    map = [[1]*m for _ in range(n)]
    for a,b in puddles:
        map[b-1][a-1]=0
        if a==1:
            for i in range(b, len(map)):
                map[i][0] = 0
        if b==1:
            for i in range(a, len(map[0])):
                map[0][i] = 0


    for j in range(1, len(map)):
        for i in range(1, len(map[0])):
            if map[j][i] != 0:
                map[j][i] = map[j-1][i] + map[j][i-1]

    for m in map:
        print(m)

    return map[-1][-1] % 1000000007

print(solution(4, 3, [[1, 2]]))