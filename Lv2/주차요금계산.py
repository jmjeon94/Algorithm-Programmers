from collections import defaultdict
import math

def get_diff(ins, outs):
    in_h, in_m = ins.split(':')
    out_h, out_m = outs.split(':')

    diff_h = int(out_h) - int(in_h)
    diff_m = int(out_m) - int(in_m)
    if diff_m < 0:
        diff_m += 60
        diff_h -= 1

    return diff_h * 60 + diff_m


def solution(fees, records):
    answer = []

    mins = defaultdict(int)
    logs = defaultdict(list)

    for r in records:
        time, car, inout = r.split()
        if logs[car]:
            in_time = logs[car].pop()
            mins[car] += get_diff(in_time, time)
        else:
            logs[car].append(time)

    for k, v in logs.items():
        if v:
            mins[k] += get_diff(v[0], '23:59')

    for car in sorted(mins.keys()):
        if mins[car]<fees[0]:
            answer.append(int(fees[1]))
        else:
            m = math.ceil((mins[car] - fees[0]) / fees[2])
            answer.append(int(m*fees[3]+fees[1]))

    return answer


print(solution(
    [1, 461, 1, 10], ["00:00 1234 IN"]
))
