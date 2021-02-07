def solution(n, lost, reserve):
    arr = [1] * n
    for i in range(1, n+1):
        if i in lost:
            arr[i-1]=0
        if i in reserve:
            arr[i-1]=2
    print(arr)

    for i, n in enumerate(arr):
        if arr[i]!=0:
            continue

        if i>0:
            if arr[i-1]==2:
                arr[i-1]-=1
                arr[i]+=1
                continue
        if i<len(arr)-1:
            if arr[i+1]==2:
                arr[i+1]-=1
                arr[i]+=1

    return len(arr)-arr.count(0)

print(solution(5, [2,4], [3]))

