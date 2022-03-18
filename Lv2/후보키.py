from itertools import combinations
def solution(relation):

    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(list(combinations(list(range(n_col)), i)))

    answer = []
    for keys in candidates:
        tmp = [tuple([item[k] for k in keys]) for item in relation]

        if len(set(tmp))==n_row:
            answer.append(keys)

    final = set(answer.copy())
    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if len(set(answer[i]) - set(answer[j]))==0:
                final.discard(answer[j])

    return len(final)

print(solution([["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]]))
# 2