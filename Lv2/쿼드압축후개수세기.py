answer = [0, 0]

def quad(arr):
    global answer

    target = len(arr) ** 2
    sum_ = 0
    for r in arr:
        sum_ += sum(r)

    if sum_ == 0:
        answer[0] += 1
    elif sum_ == target:
        answer[1] += 1
    else:
        tmp = arr[:len(arr)//2]
        sub_arr = []
        for r in tmp:
            sub_arr.append(r[:len(r)//2])
        quad(sub_arr)
        sub_arr = []
        for r in tmp:
            sub_arr.append(r[len(r)//2:])
        quad(sub_arr)
        tmp = arr[len(arr)//2:]
        sub_arr = []
        for r in tmp:
            sub_arr.append(r[:len(r)//2])
        quad(sub_arr)
        sub_arr = []
        for r in tmp:
            sub_arr.append(r[len(r)//2:])
        quad(sub_arr)

def solution(arr):
    global answer
    quad(arr)
    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))  # [4,9]
