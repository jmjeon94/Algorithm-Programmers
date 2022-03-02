def solution(numbers):
    answer = sum(range(0,10)) - sum(numbers)
    return answer

print(solution([5,8,4,0,6,7,9]))
