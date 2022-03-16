def solution(strings, n):
    answer = []
    lst = []
    for s in strings:
        lst.append(list(s))

    lst.sort(key=lambda x: (x[n], x[:]))
    for l in lst:
        answer.append(''.join(l))
    return answer