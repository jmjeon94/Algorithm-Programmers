def solution(n):
    arr = [[0]*n for _ in range(n)]

    # way: 0-아래, 1-오른, 2-대각
    way = 0
    val = 1
    r, c = -1, 0
    for i in range(n):
        time = n-i
        while time>0:
            if way==0: r+=1
            elif way==1: c+=1
            elif way==2: r-=1; c-=1
            arr[r][c] = val
            time -= 1
            val += 1

        way += 1
        if way>2: way=0

    answer = []
    for i, tmp in enumerate(arr):
        answer += tmp[:i+1]

    return answer

print(solution(4))