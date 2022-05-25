def solution(record):
    answer = []
    temp = []  # uid, enter / uid leave로 저장하기
    uid = {}
    for r in record:
        lst = r.split()
        if lst[0] != "Leave":
            uid[lst[1]] = lst[2]

        if lst[0] != "Change":
            tmp = lst[1] + " " + lst[0]
            temp.append(tmp)

    for t in temp:
        id, inout = t.split()
        if inout == "Enter":
            msg = uid[id] + "님이 들어왔습니다."
            answer.append(msg)
        else:
            msg = uid[id] + "님이 나갔습니다."
            answer.append(msg)
    return answer