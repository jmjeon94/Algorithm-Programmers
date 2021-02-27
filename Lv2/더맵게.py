def solution(scoville, K):
    cnt = -1
    min_ = min(scoville)
    while min(scoville)<K:

        a = scoville.pop(0)
        b = scoville.pop(0)
        scoville.insert(0, a + b*2)
        cnt+=1


    return cnt




print(solution([1,2,3,9,10,12], 7))