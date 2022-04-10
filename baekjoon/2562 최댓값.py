inputs = """3
29
38
12
57
74
40
85
61"""

inputs = list(map(int, inputs.split()))

m = max(inputs)
i = inputs.index(m) + 1

print(m)
print(i)
