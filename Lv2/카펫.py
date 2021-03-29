def solution(brown, yellow):
    num = brown + yellow
    divisors = get_divisor(num)
    # print(divisors)
    for divisor in divisors:
        rect = (divisor[0]-2) * (divisor[1]-2)
        if rect == yellow:
            return (max(divisor), min(divisor))


def get_divisor(a):
    divisors = []
    for i in range(1, int(a**(1/2)+1)):
        if a % i==0:
            divisors.append([i, a//i])
    return divisors

print(solution(24, 24))


