def get_min(n, m):
    if n > m:
        n, m = m, n

    while m%n != 0:
        n, m = m%n, n

    return n

def solution(n, m):
    return n * m // get_min(n,m)

print(solution(3, 12))