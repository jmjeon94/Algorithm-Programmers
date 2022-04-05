import heapq
def solution(jobs):

    answer = 0
    now = 0
    heap = []
    cnt = 0

    while cnt<len(jobs):

        for job in jobs :
            if job[0] <= now and job[1] > 0:
                heapq.heappush(heap, [job[1], job[0]])
                job[1] = -1

        if heap:
            duration, start_time = heapq.heappop(heap)
            now += duration
            answer += (now - start_time)
            cnt += 1
        else:
            now += 1

    return int(answer / len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]])) # 9