import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst_min = lst[0]
lst_max = lst[0]
for i in lst:
    if i < lst_min:
        lst_min = i
    if i > lst_max:
        lst_max = i

print(lst_min, lst_max)