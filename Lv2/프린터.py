def solution(priorities, location):

    q = list(range(len(priorities)))
    time = 0
    while True:
        first = priorities[0]
        if max(priorities[1:])>first:
            del priorities[0]
            priorities.append(first)

            first_q = q[time]
            del q[time]
            q.append(first_q)
        else:
            del priorities[0]
            time+=1
        if len(priorities)==1:
            break

    return q.index(location)+1

# best code
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer