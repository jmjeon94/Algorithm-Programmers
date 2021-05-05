def solution(n, money):
    arr = [1]
    for i in range(1, n+1):
        arr.append(0)
        for m in money:
            if i-m>0:
                arr[i] += arr[i-m]
                arr[i] = arr[i] % 1000000007
            elif i-m==0:
                arr[i] += 1
    print(arr)
    return arr[-1]

print(solution(5, [1,2,5]))