import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    data = list(input().split())
    if data[0] == "push_back":
        q.append(data[1])
    elif data[0] == "push_front":
        q.appendleft(data[1])
    elif data[0] == "pop_front" and q:
        print(q.popleft())
    elif data[0] == "pop_front" and len(q) == 0:
        print(-1)
    elif data[0] == "pop_back" and q:
        print(q.pop())
    elif data[0] == "pop_back" and len(q) == 0:
        print(-1)
    elif data[0] == "size":
        print(len(q))
    elif data[0] == "front" and q:
        print(q[0])
    elif data[0] == "front" and len(q) == 0:
        print(-1)
    elif data[0] == "back" and q:
        print(q[-1])
    elif data[0] == "back" and len(q) == 0:
        print(-1)
    elif data[0] == "empty" and len(q) == 0:
        print(1)
    elif data[0] == "empty" and q:
        print(0)

