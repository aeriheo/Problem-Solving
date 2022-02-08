import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
q = deque([[a, 0]])
result = -1
while q:
    num, cnt = q.popleft()
    if num == b :
        result = cnt +1
        break
    if num*2<=b:
        q.append([num*2, cnt+1])
    tmp = str(num) + '1'
    if int(tmp)<=b:
        q.append([int(tmp), cnt+1])

print(result)