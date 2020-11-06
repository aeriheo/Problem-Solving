def solution(a, b):
    answer = ''
    #31 = 1, 3, 5, 7, 8, 10, 12
    #29 = 2
    #30 = 4,6, 9, 11
    d = 0
    if a == 1:
        d = b
    elif a == 2:
        d = 31 + b
    elif a == 3 :
        d = 31 + 29 + b
    elif a == 4 :
        d = (31*2) + 29 + b
    elif a == 5:
        d = (31 * 2) + 30 + 29 + b
    elif a == 6:
        d = (31 * 3) + 29 + 30 + b
    elif a == 7 :
        d = (31 * 3) + (30 * 2) + 29 + b
    elif a == 8:
        d = (31 * 4) + (30 * 2) + 29 + b
    elif a == 9 :
        d = (31 * 5) + (30 * 2) + 29 + b
    elif a == 10 :
        d = (31 * 5) + (30 * 3) + 29 + b
    elif a == 11 :
        d = (31 * 6) + (30 * 3 ) + 29 + b
    else:
        d = (31 * 6) + (30 * 4) + 29 + b

    w = d % 7
    # 1 = 금 2 = 토 3 = 일 4 = 월 5 = 화 6 = 수 0 = 목
    if w == 0:
        answer = 'THU'
    elif w == 1:
        answer = 'FRI'
    elif w == 2:
        answer = 'SAT'
    elif w == 3:
        answer = 'SUN'
    elif w == 4:
        answer = 'MON'
    elif w == 5:
        answer = 'TUE'
    else:
        answer = 'WED'
    return answer

print(solution(5,24))

