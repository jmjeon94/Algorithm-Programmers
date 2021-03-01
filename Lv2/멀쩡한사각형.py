def gcd(a, b):
    return b if a%b==0 else gcd(b, a%b)

def solution(w,h):
    return w*h - (w+h-gcd(w,h))

print(solution(8, 12))