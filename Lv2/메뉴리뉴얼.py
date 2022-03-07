from itertools import combinations
from collections import Counter, defaultdict
import heapq
def solution(orders, course):

	counter = defaultdict(int)
	candidates = defaultdict(list)
		
	answer = []
	for order in orders:
		for c in course:
			for comb in combinations(sorted(order), c):
				counter[comb] += 1
	# print(counter)

	for k, v in counter.items():
		heapq.heappush(candidates[len(k)], (-v, (k, v)))
	# print(candidates)

	for k, v in candidates.items():
		max_ = 2
		for i in range(len(candidates[k])):
			_, (tmp_str, tmp_val) = heapq.heappop(candidates[k])
			if max_ <= tmp_val:
				max_ = tmp_val
				answer.append(''.join(tmp_str))
	# print(answer)

	return sorted(answer)


def solution2(orders, course):
	result = []
	for course_size in course:
		order_combinations = []
		for order in orders:
			order_combinations += combinations(sorted(order), course_size)

		most_ordered = Counter(order_combinations).most_common()
		result += [''.join(k) for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

	return sorted(result)


print(solution2(["XYZ", "XWY", "WXA"], [2,3,4]))



