def solution(dirs):
    stack = []
    cur = [0, 0]
    prev = [0, 0]
    for d in dirs:
        if d=='U':
            cur[0] += 1
            cur[0] = min(cur[0], 5)
        elif d=='D':
            cur[0] -= 1
            cur[0] = max(cur[0], -5)
        elif d=='L':
            cur[1] -= 1
            cur[1] = max(cur[1], -5)
        elif d=='R':
            cur[1] += 1
            cur[1] = min(cur[1], 5)
        if prev+cur not in stack and cur+prev not in stack and prev!=cur:
            stack.append((prev+cur).copy())
            stack.append((cur+prev).copy())
        prev = cur.copy()
    # print(stack)
    return len(stack)//2

print(solution('ULURRDLLU')) # 7