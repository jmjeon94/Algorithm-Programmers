def cnt_updown(target):
    cur='A'
    diff = abs(ord(target)-ord(cur))
    diff_reverse = 26 - diff
    return min(diff, diff_reverse)

def solution(name):
    answer = 0
    target='A' * len(name)
    cur = 0
    while name!=target:
        min_diff = 21
        for i in range(len(target)):
            if target[i] != name[i]:
                diff = abs(cur - i)
                diff = min(diff, len(target)-diff)
                if min_diff>diff:
                    min_idx = i
                    min_diff = diff
        cur = min_idx
        answer += min_diff
        answer += cnt_updown(name[cur])
        target = target[:cur] + name[cur] + target[cur+1:]

    return answer

print(solution('JEROEN')) # 56