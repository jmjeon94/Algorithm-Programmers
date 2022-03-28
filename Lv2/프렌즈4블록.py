def solution(m, n, board):
    board = list(map(list, zip(*board))) # 행열 바꾸기
    m, n = n, m
    # for i in range(m):
    #     print(board[i])
    while True:
        correct = []

        for i in range(m):
            for j in range(n):
                if i == m - 1 or j == n - 1:
                    continue
                ref = board[i][j]
                if ref != '0' and ref == board[i][j + 1] and ref == board[i + 1][j] and ref == board[i + 1][j + 1]:
                    correct.append([i, j])
        if not correct:
            break
        #
        # print(correct)
        for cy, cx in correct:
            board[cy][cx] = '0'
            board[cy + 1][cx] = '0'
            board[cy][cx + 1] = '0'
            board[cy + 1][cx + 1] = '0'


        # for i in range(m):
        #     print(board[i])
        # print()

        # reset board
        for i in range(m):
            chs = []
            for j in range(n):
                if board[i][j]!='0':
                    chs.append(board[i][j])
            if chs:
                board[i] = list('0'*(n-len(chs))+ ''.join(chs))

        # for i in range(m):
        #     print(board[i])

    answer = 0
    for i in range(m):
        # print(board[i])
        answer += board[i].count('0')

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
