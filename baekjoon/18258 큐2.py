import sys
from collections import deque
n = int(input())


q = deque()
for _ in range(n):
    order = sys.stdin.readline()

    if order.startswith('push'):
        q.append(order.split()[1])
    elif order.startswith('front'):
        print(q[0] if q else -1)
    elif order.startswith('back'):
        print(q[-1] if q else -1)
    elif order.startswith('size'):
        print(len(q))
    elif order.startswith('empty'):
        print(int(len(q)==0))
    elif order.startswith('pop'):
        print(q.popleft() if q else -1)
