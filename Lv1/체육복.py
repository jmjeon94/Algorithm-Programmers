def solution(n, lost, reserve):

    for r in reserve.copy():
        if r in lost:
            reserve.remove(r)
            lost.remove(r)

    for r in reserve:
        for l in lost:
            if r-1==l or r+1==l:
                lost.remove(l)
                break

    return n - len(lost)

print(solution(5, [2,4], [3]))


