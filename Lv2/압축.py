def solution(msg):
    keys = {}
    for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        keys[c] = i + 1
    answer = []

    skip = 0
    for i, ch in enumerate(msg):
        if skip > 0:
            skip -= 1
            continue
        for j in range(len(msg) - i):

            target = msg[i:len(msg) - j]
            if target in keys:
                answer.append(keys[target])
                keys[msg[i:len(msg) - j + 1]] = len(keys) + 1
                skip = len(target) - 1

                break
    return answer


print(solution('KAKAO'))
