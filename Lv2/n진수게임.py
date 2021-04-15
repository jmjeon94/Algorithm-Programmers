def int2char(n):
    if n>=10:
        n -= 10
        return chr(ord('A')+n)
    else: return str(n)

def get_n(i, n):
    answer = ''
    while i>=n:
        i, tmp = i//n, i%n
        answer = int2char(tmp) + answer
    return int2char(i) + answer

def solution(n, t, m, p):
    answer = ''
    i=0
    while len(answer)<t*m:
        answer += get_n(i, n)
        i+=1

    return answer[p-1::m][:t]

print(solution(2,4,2,1))