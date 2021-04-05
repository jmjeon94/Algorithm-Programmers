def solution(n, words):
    prev = words[0][0]
    for i, word in enumerate(words):
        person = (i+1)%n if (i+1)%n!=0 else n
        nth = i//n+1

        # 틀린경우
        if prev[-1]!=word[0]:
            return [person,  nth]

        # 중복된 경우
        if word in words[:i]:
            return [person, nth]

        prev = word

    # 문제 없는 경우
    return [0, 0]

print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))