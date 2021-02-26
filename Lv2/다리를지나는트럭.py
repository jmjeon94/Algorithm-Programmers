def solution(bridge_length, weight, truck_weights):
    in_cnt = 0
    out_cnt = 0
    time = 0
    q = []
    while out_cnt<len(truck_weights):
        time+=1

        if in_cnt<len(truck_weights):
            q.append([0, truck_weights[in_cnt]])

            if sum(x[1] for x in q if x[0]<bridge_length)>weight:
                q.pop()
            else:
                in_cnt += 1

        for truck in q:
            truck[0]+=1

        if q[0][0]==bridge_length+1:
            q.pop(0)
            out_cnt += 1

    return time

