def get_diff(cur, target):
    h = 4 if cur in ['*', '#', 0] else (cur+2)//3
    target_h = (target+1)//3 if target!=0 else 4
    
    if cur in [2,5,8,0]:
        return abs(h-target_h)
    else:
        return abs(h-target_h)+1
    
def solution(numbers, hand):
    answer = ''

    cur = {'left':'*',
           'right':'#'}
    
    for n in numbers:
        if n in [1,4,7]:
            cur['left'] = n
            answer += 'L'
        elif n in [3,6,9]:
            cur['right'] = n
            answer += 'R'
        else:
            left = get_diff(cur['left'], n)
            right = get_diff(cur['right'], n)
            if left==right:
                cur[hand] = n
                answer += hand[:1].upper()
            elif left>right:
                cur['right'] = n
                answer += 'R'
            else:
                cur['left'] = n
                answer += 'L'
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))