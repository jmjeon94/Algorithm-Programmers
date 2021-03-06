def check(p):
    stack = []
    for ch in p:
        if ch==')':
            if stack and stack[-1]=='(':
                stack.pop()
                continue
            else:
                return False
        stack.append(ch)
    return len(stack)==0

def reverse(p):
    result = ''
    for i, ch in enumerate(p):
        if ch=='(': result += ')'
        elif ch==')': result += '('
    return result

def solution(p):
    if len(p)==0: return p
    if check(p): return p

    lcnt, rcnt = 0, 0
    for i, ch in enumerate(p):
        lcnt += int(ch=='(')
        rcnt += int(ch==')')
        if lcnt==rcnt:
            break

    u, v = p[:i+1], p[i+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')' + reverse(u[1:-1])

    return answer

print(solution(')()()()('))