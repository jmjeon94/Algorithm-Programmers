def solution(sizes):
    max1, max2 = 0, 0

    for s in sizes:
        m1, m2 = max(s), min(s)

        max1 = max(max1, m1)
        max2 = max(max2, m2)

    return max1 * max2