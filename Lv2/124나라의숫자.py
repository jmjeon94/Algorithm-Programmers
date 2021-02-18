def solution(n):
    answer = ''
    nums = ['4', '1', '2']
    while True:
        answer = nums[n%3] + answer
        n = n//3 - (n%3 == 0)
        if n==0: break

    return answer

print(solution(15))

'''
1 2  3  4  5  6  7 8  9  10 11 12  13  14  15  16  17  18  19  20
1 2  4 11 12 14 21 22 24 41 42 44 111 112 114 121 122 124 141 142 
'''