inputs = """10
1
3
5
4
0
0
7
0
0
6"""
n, *inputs = list(map(int, inputs.split()))
print(inputs)

stack = []
for i in inputs:
    if i==0:
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))