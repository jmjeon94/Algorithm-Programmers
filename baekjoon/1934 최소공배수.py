n = int(input())


def get_gcd(x, y):
    x, y = max(x, y), min(x, y)
    while x % y:
        x, y = y, x % y

    return y


for _ in range(n):
    a, b = list(map(int, input().split()))

    m = get_gcd(a, b)
    print(a * b // m)

