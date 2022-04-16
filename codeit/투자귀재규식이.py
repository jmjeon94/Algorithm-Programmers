def sublist_max(profits):
    best = 0
    for i, p in enumerate(profits):
        sum_ = p
        for j, pp in enumerate(profits[i+1:]):
            sum_ += pp
            best = max(best, sum_)
    return best

# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))