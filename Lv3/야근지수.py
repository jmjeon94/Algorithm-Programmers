import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)

    for i in range(n):
        a = heapq.heappop(works)
        heapq.heappush(works, a+1 if a<0 else 0)

    answer = sum([x**2 for x in works])
    return answer

print(solution(4, [4,3,3]))