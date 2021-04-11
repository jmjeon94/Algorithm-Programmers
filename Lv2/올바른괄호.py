def solution(s):
    stack = []
    for ch in s:
        if ch=='(':
            stack.append(ch)
        elif ch==')':

            if len(stack)==0:
                return False
            else:
                stack.pop()

    return len(stack)==0


print(solution('(()())'))