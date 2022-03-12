n = 5
inputs = """3 4
1 1
1 -1
2 2
3 3"""

nums = inputs.split('\n')
nums = list(map(lambda x: list(map(int,x.split())), nums))

for i in sorted(nums, key=lambda x:(x[1], x[0])):
    print(i[0], i[1])
