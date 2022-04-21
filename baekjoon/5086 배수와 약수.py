inputs_str = """8 16
32 4
17 5
0 0"""

inputs = []
for x in inputs_str.split("\n"):
    a, b = x.split()
    inputs.append([int(a), int(b)])

for a, b in inputs:
    if a==0 and b==0:
        break

    if a%b==0:
        print('multiple')

    elif b%a==0:
        print('factor')

    else:
        print('neither')