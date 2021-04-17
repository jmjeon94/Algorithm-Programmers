from itertools import combinations
from collections import Counter

def solution(orders, course):
		
	answer = []
	for order in orders:
		for ch in order:
			answer.append(ch)
	print(Counter(answer))

	return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
