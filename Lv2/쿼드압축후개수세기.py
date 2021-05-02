def sum(arr, r, c, size):
    cnt = 0
    for row in arr[r:r+size]:
        for val in row[c:c+size]:
            cnt+=val
    if cnt==size**2:
        return 1
    elif cnt==0:
        return 0
    else: return 2

def solution(arr):
    answer = []
    print(sum(arr, 0, 2, 2))
    return answer

print(solution([[1,1,0,0],[1,1,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]