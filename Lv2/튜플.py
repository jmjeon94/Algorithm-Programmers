def solution(s):
    answer = []
    list_ = s.split('{')
    list_ = list(filter(lambda x:x, list_))
    list_ = list(map(lambda x:x.replace('}', ''), list_))
    list_ = sorted(list_, key=lambda x:len(x))
    
    tmp = []
    for li in list_:
        if li[-1]==',':
            li=li[:-1]
        tmp.append(set(map(lambda x: int(x), li.split(','))))

    answer = []
    prev_set = set()
    for cur_set in tmp:
        answer.append(list(cur_set-prev_set)[0])
        prev_set = cur_set
        
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))