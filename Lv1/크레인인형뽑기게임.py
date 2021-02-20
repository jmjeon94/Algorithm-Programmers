def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for row in board:
            if row[m-1]>0:
                new = row[m-1]
                row[m-1] = 0

                if stack[-1:]==[new]:
                    stack = stack[:-1]
                    answer+=2
                else:
                    stack.append(new)
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4