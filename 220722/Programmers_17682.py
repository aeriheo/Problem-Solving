def solution(dartResult):
    answer = 0
    sdt = [0] * 3
    dartResult = list(dartResult)

    lst = []
    num = []

    for d in dartResult:
        if d == "#" or d == "*":
            lst.append(d)
            continue
        if d == "D" or d == "S" or d == "T":
            lst.append(int(''.join(num)))
            lst.append(d)
            num = []
        else:
            num.append(d)

    sdt = []
    for i in range(len(lst)):
        if lst[i] == "S":
            sdt.append(lst[i - 1])
        elif lst[i] == "D":
            sdt.append((lst[i - 1]) ** 2)
        elif lst[i] == "T":
            sdt.append((lst[i - 1]) ** 3)
        elif lst[i] == "*":
            if len(sdt) >= 2:
                sdt[-2] *= 2
                sdt[-1] *= 2
            else:
                sdt[-1] *= 2
        elif lst[i] == "#":
            sdt[-1] *= (-1)

    answer = sum(sdt)

    return answer