def solution(progresses, speeds):
    answer = []

    for i in range(100):
        for j in range(len(progresses)):
            progresses[j] += speeds[j]
        cnt = 0

        # 100%가 넘는 progresses의 순차적 개수 카운팅
        for prog in progresses:
            if prog>=100:
                cnt+=1
            else:
                break
        for c in range(cnt):
            del progresses[0]
            del speeds[0]

        if cnt>0:
            answer.append(cnt)
        # 종료 조건
        if progresses==[]:
            break

    return answer