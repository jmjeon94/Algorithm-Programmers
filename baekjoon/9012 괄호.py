def check(ps):
    stack = []

    for ch in ps:
        if ch=='(':
            stack.append(ch)
        elif ch==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

n = int(input())

for _ in range(n):
    print('YES' if check(input()) else 'NO')