def ten2two(t, n):
    arr = []
    while n//2!=0:
        arr.append(n%2)
        n = n//2
    arr += [n%2]
    arr = arr[::-1]
    arr = [0] * (t-len(arr)) + arr
    return arr
ten2two(5, 10)

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = ''
        a, b = ten2two(n, a), ten2two(n, b)

        for i in range(len(a)):
            row += '#' if a[i] or b[i] else ' '
        answer.append(row)
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.zfill(n)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))