import sys
def array_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]>lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst

T = int(sys.stdin.readline())
for _ in range(T):
    a = list(map(int, sys.stdin.readline().split()))
    lst = array_sort(a)
    print(lst[7])