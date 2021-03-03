def solution(s):
    min_ = len(s)
    for n in range(1, len(s)//2+1):

        arr = [s[i:i+n] for i in range(0, len(s), n)]

        word = ''
        prev_ch = ''
        duplicate_cnt = 1
        for ch in arr:
            if prev_ch!=ch:
                word += ch
                if duplicate_cnt != 1:
                    word += str(duplicate_cnt)
                duplicate_cnt = 1

            else:
                duplicate_cnt += 1
            prev_ch = ch

        if duplicate_cnt != 1:
            word += str(duplicate_cnt)

        min_ = min(min_, len(word))

    return min_

print(solution('abcabcabcabcdededededede'))
