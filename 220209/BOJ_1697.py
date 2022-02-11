import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque([[n, 0]])
result = 0
while q:
    now, cnt = q.popleft()
    if now == k:
        result = cnt
        break
    if now - 1 >=0:
        q.append([now-1, cnt+1])
    if now + 1 <= 100000:
        q.append([now+1, cnt+1])
    if now * 2 <= 100000:
        q.append([now*2, cnt+1])
print(result)