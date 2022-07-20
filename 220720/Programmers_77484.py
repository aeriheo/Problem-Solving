def solution(lottos, win_nums):
    answer = []
    win_nums.sort()
    lottos.sort()
    up = 0
    down = 0
    zero_cnt = lottos.count(0)
    if zero_cnt != 0:
        for i in lottos[zero_cnt - 1:]:
            if i in win_nums:
                up += 1
                down += 1
    else:
        for i in lottos:
            if i in win_nums:
                up += 1
                down += 1

    up += zero_cnt

    if up == 6:
        answer.append(1)
    elif up == 5:
        answer.append(2)
    elif up == 4:
        answer.append(3)
    elif up == 3:
        answer.append(4)
    elif up == 2:
        answer.append(5)
    else:
        answer.append(6)

    if down == 6:
        answer.append(1)
    elif down == 5:
        answer.append(2)
    elif down == 4:
        answer.append(3)
    elif down == 3:
        answer.append(4)
    elif down == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer