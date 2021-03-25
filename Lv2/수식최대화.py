from itertools import permutations

def split(strings):
    nums = []
    calcs = []

    tmp = ''
    for i, ch in enumerate(strings):
        if ch in ['*', '-', '+']:
            calcs.append(ch)
            if i==0: continue
            nums.append(int(tmp))
            tmp = ''
        else:
            tmp += ch
    nums.append(int(tmp))
    return nums, calcs


def solution(expression):
    seqs = list(permutations(['+','-','*'], 3))
    # print(seqs)
    max_ = 0

    for seq_list in seqs:
        nums, calcs = split(expression)
        for seq in seq_list:
            while seq in calcs:
                i = calcs.index(seq)
                op = calcs.pop(i)
                if op=='-':
                    nums[i] = nums[i] - nums[i+1]
                elif op=='*':
                    nums[i] = nums[i] * nums[i+1]
                elif op=='+':
                    nums[i] = nums[i] + nums[i+1]
                nums.pop(i+1)

                print(nums, calcs)

        max_ = max(max_, abs(nums[0]))

    return max_

print(solution("1*3-4*3")) # 300