import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    lst_set = set(lst)

    # 같은 눈이 4개
    if len(lst_set) == 1:
        lst_set = list(lst_set)
        arr.append(50000 + (lst_set[0]* 5000))

    elif len(lst_set) == 2:
        lst_set = list(lst_set)
        # 같은 눈이 3개
        if lst.count(lst_set[0]) == 3:
            arr.append(10000 + (lst_set[0] * 1000))
        elif lst.count(lst_set[1]) == 3:
            arr.append(10000 + (lst_set[1] * 1000))
        # 같은 눈이 2개씩 2쌍
        elif lst.count(lst_set[0]) == 2:
            arr.append(2000 + (lst_set[0] * 500) + (lst_set[1] * 500))

    elif len(lst_set) == 3:
        # 같은 눈이 2개
        lst_set = list(lst_set)
        if lst.count(lst_set[0]) == 2:
            arr.append(1000 + (lst_set[0] * 100))
        elif lst.count(lst_set[1]) == 2:
            arr.append(1000 + (lst_set[1] * 100))
        elif lst.count(lst_set[2]) == 2:
            arr.append(1000 + (lst_set[2] * 100))

    elif len(lst_set) == 4:
        arr.append(max(lst) * 100)

print(max(arr))