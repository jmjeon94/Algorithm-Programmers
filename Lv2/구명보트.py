import collections

def solution(people, limit):
    people.sort(reverse=True)
    people = collections.deque(people)
    answer = 0
    while len(people)>0:
        if len(people)==1:
            return answer + 1
        if people[0] + people[-1] <= limit:
            people.pop()
        people.popleft()
        answer += 1

    return answer

print(solution([70, 50, 80], 100)) # 3
