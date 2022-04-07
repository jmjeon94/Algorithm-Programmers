answer = []
def hanoi(fr, to, mid, n):
    global answer
    if n==1:
        answer.append([fr, to])
        return
    hanoi(fr, mid, to, n-1)
    answer.append([fr, to])
    hanoi(mid, to, fr, n-1)

def solution(n):
    global answer
    hanoi(1, 3, 2, n)
    return answer
