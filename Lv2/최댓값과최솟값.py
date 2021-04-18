def solution(s):
    nums = [int(n) for n in s.split()]
    return f'{min(nums)} {max(nums)}'

print(solution("1 2 3 4"))