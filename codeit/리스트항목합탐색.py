def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    l, r = 0, len(sorted_list) - 1
    while l < r:
        sum_ = sorted_list[l] + sorted_list[r]
        if sum_ == search_sum:
            return True
        if sum_ > search_sum:
            r -= 1
        else:
            l += 1
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))