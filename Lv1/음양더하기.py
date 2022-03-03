def solution(absolutes, signs):

    answer = 0
    for n, b in zip(absolutes, signs):
        answer += n if b else -n

    return answer