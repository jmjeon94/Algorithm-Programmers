def ten2three(n):
    three = ''
    while n!=0:
        n, extra = n//3, n%3
        three = str(extra) + three
    return three

def three2ten(n):
    ten = 0
    for i, s in enumerate(n):
        ten += int(int(s) * (3**i))
    return ten

def solution(n):
    return three2ten(ten2three(n))

print(solution(11))