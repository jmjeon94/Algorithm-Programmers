def solution(s):
    answer = ''
    i=0
    for ch in s:
        if ch==' ':
            answer += ch
            i=0
        else:
            answer += ch.upper() if i%2==0 else ch.lower()
            i+=1
    return answer

print(solution('try   hello world a aa aaa aaaa  '))
