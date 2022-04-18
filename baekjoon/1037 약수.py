n = int(input())
nums = sorted(list(map(int, input().split())))


if n%2==0:
    print(nums[n//2-1]*nums[n//2])
else:
    print(nums[n//2]**2)