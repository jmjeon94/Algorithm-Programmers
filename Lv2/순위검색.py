import bisect
from collections import defaultdict
from itertools import combinations


def solution(info, query):

    answer = []

    dictionary = defaultdict(list)
    for i in info:
        *info_, val = i.split()

        for i in range(5):
            for k in list(combinations(info_,i)):
                dictionary[''.join(k)].append(int(val))

    for d in dictionary:
        dictionary[d].sort()

    for q in query:
        q = q.replace('and', '')
        *cond, val = q.split()
        while '-' in cond:
            cond.remove('-')
        scores = dictionary[''.join(cond)]
        idx = bisect.bisect_left(scores, int(val))
        answer.append(len(scores) - idx)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))