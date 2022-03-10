def hanoi(fr, to, mid, n):
    if n == 1:
        print(fr, to)
        return

    hanoi(fr, mid, to, n - 1)
    print(fr, to)
    hanoi(mid, to, fr, n - 1)

k = 3 # input()
print(2**k-1)
hanoi(1, 3, 2, k)