from collections import Counter

def solution(N, stages):

    cnt = Counter(stages)
    cnt = sorted(cnt.items(), key=lambda x: x[0])

    answer = []
    empty_list = []

    total = len(stages)
    i = 1
    j = 0
    while i<N+1 and j<len(cnt):

        n, c = cnt[j]
        if i!=n:
            empty_list.append(i)
            i+=1
            continue

        # print(f'{c}/{total}')
        answer.append((i, c/total))
        total -= c
        i+=1
        j+=1

    empty_list += range(i, N+1)

    answer = sorted(answer, key=lambda x:x[1], reverse=True)
    ans = [x[0] for x in answer] + empty_list

    return ans

print(solution(4, [1]))