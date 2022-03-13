import sys
n = 13
words = """
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours"""

words = words.split()

for w in sorted(list(set(words)), key=lambda x:(len(x), x)):
    print(w)
