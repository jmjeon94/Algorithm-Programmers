def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    n_zero = lottos.count(0)
    n_correct = 0

    for l in lottos:
        if l in win_nums:
            n_correct += 1

    return [rank[n_zero + n_correct], rank[n_correct]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
