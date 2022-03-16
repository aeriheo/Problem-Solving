def solution(s):
    answer = ''
    low = []
    up = []
    for i in list(s):
        if i.isupper():
            up.append(i)
        else:
            low.append(i)

    up.sort(reverse=True)
    low.sort(reverse=True)
    u = ''.join(up)
    l = ''.join(low)
    answer = l + u
    return answer