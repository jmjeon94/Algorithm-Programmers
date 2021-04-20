import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0]<K and len(scoville)>=2:

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a+b*2)
        cnt+=1

    if scoville[0]>=K:
        return cnt
    else: return -1

print(solution([1,1,1,8], 7))

