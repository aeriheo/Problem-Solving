import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
result = 9876543210
cnt = 0
q = deque([[n, 0]])
visited = [False] * 100001
while q:
    now, move = q.popleft()

    visited[now] = True

    if now == k :
        if move < result:
            cnt = 1
            result = move
        elif move == result:
            cnt += 1
        else: break
        continue


    if now-1 >= 0 and visited[now-1] != True:
        q.append([now-1, move+1])
    if now+1<100001 and visited[now+1] != True:
        q.append([now+1, move+1])
    if now*2<100001 and visited[now*2] != True:
        q.append([now*2, move+1])


print(result)
print(cnt)