def solution(record):
    msgs = []
    answer = []
    _dict = {}
    for r in record:

        r = r.split()
        order, uid = r[:2]
        if len(r)==3:
            name = r[-1]

        if order in ['Enter', 'Leave']:
            msgs.append([order, uid])

        if order in ['Enter', 'Change']:
            _dict[uid] = name


    for order, uid in msgs:
        name = _dict[uid]
        msg_last = '님이 들어왔습니다.' if order=='Enter' else '님이 나갔습니다.'
        msg = f'{name}{msg_last}'
        answer.append(msg)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))