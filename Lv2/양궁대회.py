answers = []
visited = []
max_ = 0


def dfs(v, target, goals):
    global answers, max_, visited

    visited[v] += 1

    if sum(visited) == target:
        score_diff = 0
        for i, (vi, g) in enumerate(zip(visited, goals)):
            diff = 10 - i
            if g == 1 and vi == 0:
                continue
            elif g - 1 < vi:
                score_diff += diff
            elif g - 1 >= vi:
                score_diff -= diff
        # print(visited, goals, score_diff)

        if max_ <= score_diff:
            # print('ans', visited)
            max_ = score_diff
            answers.append([visited.copy(), max_])

    for w in range(v, 11):
        if visited[w] < goals[w] and target >= sum(visited) + 1:
            dfs(w, target, goals)

    visited[v] -= 1


def solution(n, info):
    global answers, visited
    # print(info)

    goals = []
    for i in info:
        goals.append(i + 1)
    for i in range(11):
        # print('start', i)
        visited = [0] * 11
        dfs(i, n, goals)

    if not answers or max_==0:
        return [-1]
    else:
        answers = [ans for ans in answers if ans[1]==max_]
        answers.sort(key=lambda x: x[0][::-1], reverse=True)
        return answers[0][0]

print(solution(n=9, info=[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))