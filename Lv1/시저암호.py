def solution(s, n):
    answer = []
    for ch in s:
        if ch == ' ':
            answer.append(ch)
            continue
        new = ord(ch) + n
        if (ord(ch)>97 and new>=97+26) or (ord(ch)<97 and new>=65+26):
            new -= 26
        answer.append(chr(new))
    return ''.join(answer)

print(solution("a", 4))
