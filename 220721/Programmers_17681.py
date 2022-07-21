def solution(n, arr1, arr2):
    answer = []
    lst1 = []
    lst2 = []
    for a in arr1:
        temp = []
        while a > 1:
            temp.insert(0, a % 2)
            a = int(a / 2)
        if a == 1: temp.insert(0, 1)
        while len(temp) < n:
            temp.insert(0, 0)
        lst1.append(temp)

    for a in arr2:
        temp = []
        while a > 1:
            temp.insert(0, a % 2)
            a = int(a / 2)
        if a == 1: temp.insert(0, 1)
        while len(temp) < n:
            temp.insert(0, 0)
        lst2.append(temp)

    for x in range(n):
        temp = []
        for y in range(n):
            if lst1[x][y] == 1 or lst2[x][y] == 1:
                temp.append("#")
            else:
                temp.append(" ")
        answer.append(''.join(temp))

    return answer