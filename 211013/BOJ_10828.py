import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    lst = list(input().split())
    if lst[0] == "push":
        data.append(lst[1])
    if lst[0] == "top" and data:
        print(data[-1])
    elif lst[0] == "top" and len(data) == 0:
        print(-1)
    if lst[0] == "size":
        print(len(data))
    if lst[0] == "empty" and data:
        print(0)
    elif lst[0] == "empty" and len(data) == 0:
        print(1)
    if lst[0] == "pop" and data:
        print(data.pop())
    elif lst[0] == "pop" and len(data) == 0:
        print(-1)