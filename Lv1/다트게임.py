def solution(dartResult):
    answer = []
    for i, ch in enumerate(dartResult):
        if ch.isdigit():
            if ch=='0' and len(answer)>0 and answer[-1]==1:
                answer[-1] = 10
            else:
                answer.append(int(ch))
            
        elif ch == '*':
            answer[-1] = answer[-1]*2
            if len(answer)>1:
                answer[-2] = answer[-2]*2
        elif ch =='#':
            answer[-1] = -answer[-1]
            
        elif ch=='S':
            continue
        elif ch=='D':
            answer[-1] = answer[-1]**2
        elif ch=='T':
            answer[-1] = answer[-1]**3

    return sum(answer)

print(solution('1D2S#10S')) # 9