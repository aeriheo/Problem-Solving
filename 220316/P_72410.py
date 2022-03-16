from collections import deque

def solution(new_id):
    answer = ''
    lst = list(new_id)
    # 1단계
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i] = lst[i].lower()

    # 2단계
    lst = deque(lst)
    for _ in range(len(lst)):
        p = lst.popleft()
        if p == "-" or p.islower() or p == '.' or p == '_' or p.isnumeric():
            lst.append(p)

    # 3단계
    if lst:
        before = lst.popleft()
        lst.append(before)
    for _ in range(1, len(lst)):
        p = lst.popleft()
        if before == '.' and before == p: continue
        before = p
        lst.append(p)

    # 4단계
    while lst and lst[0] == ".":
        lst.popleft()

    while lst and lst[-1] == ".":
        lst.pop()

    # 5단계
    if len(lst) == 0:
        lst.append("a")

    # 6단계
    if len(lst) > 15:
        l = list(lst)
        lst = l[:15]
        lst = deque(lst)
        if lst[-1] == ".":
            while lst and lst[-1] == ".":
                lst.pop()

    # 7단계
    if len(lst) <= 2:
        last = lst[-1]
        while len(lst) < 3:
            lst.append(last)

    lst = list(lst)
    answer = ''.join(lst)
    return answer