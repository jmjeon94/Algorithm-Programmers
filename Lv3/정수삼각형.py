def solution(triangle):

    for j, n in enumerate(triangle):
        if j==0: continue
        for i, m in enumerate(triangle[j]):
            if i==0:
                triangle[j][i] += triangle[j-1][0]
            elif i==len(triangle[j])-1:
                triangle[j][i] += triangle[j-1][j-1]
            else:
                triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])

    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30