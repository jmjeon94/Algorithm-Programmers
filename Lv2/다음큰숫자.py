def solution(n):

    cnt = bin(n).count('1')
    n += 1
    while cnt!=bin(n).count('1'):
        n += 1

    return n

print(solution(78)) #83
