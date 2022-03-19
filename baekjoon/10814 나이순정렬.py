inputs = """3
21 Dohyun
21 Junkyu
20 Sunyoung"""


n, *data = inputs.split('\n')
print(n, data)

for d in sorted(data, key=lambda x:int(x.split()[0])):
    print(d)
