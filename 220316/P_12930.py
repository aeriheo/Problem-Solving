def solution(s):
    answer = ''
    lst = list(s)
    idx = 0
    for i in range(len(s)):
        if lst[i] == " ":
            idx = 0
            continue

        if idx % 2 == 0:
            lst[i] = lst[i].upper()
        else:
            lst[i] = lst[i].lower()
        idx += 1

    answer = ''.join(lst)
    return answer