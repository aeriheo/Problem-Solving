def solution(s):
    answer = []
    s = s[1:-1]
    dic = []
    lst = []

    for i in s:
        if i == "}":
            if len(num) == 0: pass
            lst.append(int(''.join(num)))
            dic.append(lst)
            num = []
            lst = []
        elif i == ",":
            if len(num) == 0: continue
            lst.append(int(''.join(num)))
            num = []
        elif i == "{":
            num = []
        else:
            num.append(i)

    dic.sort(key=lambda x: len(x))

    for i in range(len(dic)):
        for j in range(len(dic[i])):
            if dic[i][j] not in answer:
                answer.append(dic[i][j])
    return answer