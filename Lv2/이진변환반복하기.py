def solution(s):
    cnt_0, cnt_b = 0, 0
    while s != '1':
        cnt_0 += s.count('0')
        cnt_b += 1
        s = bin(len(s.replace('0', '')))[2:]

    return [cnt_b, cnt_0]

print(solution('110010101001')) # [3, 8]