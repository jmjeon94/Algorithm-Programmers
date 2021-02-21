def solution(s):
    answer = ''
    words = [word[0].upper() + word[1:] for word in s.lower().split()]

    i = 0
    word_cnt = 0
    for ch in s.lower():
        if not ch.isalnum():
            answer += ch
            word_cnt = 0
        else:
            if word_cnt>0:
                continue
            else:
                answer += words[i]
                word_cnt+=1
                i+=1

    return answer

print(solution('  Hello     World'))