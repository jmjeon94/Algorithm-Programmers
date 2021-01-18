def solution(n):
    word = '수박'
    return word*(n//2) + word[:n%2]

print(solution(4))