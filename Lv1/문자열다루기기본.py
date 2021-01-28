def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)

print(solution('1234'))