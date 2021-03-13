def split(string):
    s = []
    for a, b in zip(string, string[1:]):
        if (a+b).isalpha():
            s.append((a+b).lower())
    return s

def solution(str1, str2):
    s1 = split(str1)
    s2 = split(str2)
    
    len_s2 = len(s2)
    
    for ch in s1:
        try:
            s2.remove(ch)
        except:
            pass
    
    inter = len_s2 - len(s2)
    union = len(s1) + len(s2)
    
    return int(inter/union*65536) if union else 65536

print(solution('aa1+aa2', 'AAAA12'))
