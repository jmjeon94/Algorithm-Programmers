def solution(skill, skill_trees):
    answer = 0

    for trees in skill_trees:
        tmp = ''
        for ch in trees:
            if ch in skill:
                tmp += ch

        if skill[:len(tmp)]==tmp:
            answer+=1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))