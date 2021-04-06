def solution(nums):

    return min(len(nums)//2, len(list(set(nums))))

print(solution([3,3,3,2,2,2]))