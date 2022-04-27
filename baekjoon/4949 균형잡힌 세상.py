def check(sentence):
    stack = []
    for ch in sentence:

        if ch=='(' or ch=='[':
            stack.append(ch)
        elif ch==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif ch==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

while True:
    inputs = input()
    if inputs=='.':
        break
    print('yes' if check(inputs) else 'no')

