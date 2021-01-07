def solution(arr):
    answer = []
    prev_ch = ''
    for ch in arr:
        if ch!=prev_ch:
            answer.append(ch)
        prev_ch = ch
    return answer

print(solution([1,1,3,3,0,1,1]))
