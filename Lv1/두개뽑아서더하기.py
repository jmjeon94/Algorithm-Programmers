from itertools import combinations

def solution(numbers):
    answer = []
    for s in list(combinations(numbers, 2)):
        answer.append(sum(s))
    return sorted(list(set(answer)))