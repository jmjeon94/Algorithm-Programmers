from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))

    dec_names = defaultdict(list)
    cnts = defaultdict(int)

    for r in report:
        n = r.split(' ')
        dec_names[n[0]].append(n[1])
        cnts[n[1]] += 1

    answer = []
    for _id in id_list:
        cnt = 0
        for dec in dec_names[_id]:
            if cnts[dec] >= k:
                cnt += 1
        answer.append(cnt)

    return answer