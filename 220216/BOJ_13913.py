import sys
sys.setrecursionlimit(1000000000)
from collections import deque
input = sys.stdin.readline

def result_root(a, b):
    if a != b:
        result_root(a, root[b])
    print(b, end = ' ')

n, k = map(int, input().split())
q = deque([[n, 0]])
root = [0] * 100001
visited = [False] * 100001
visited[n] = True

while q:
    now, move = q.popleft()

    if now == k :
        print(move)
        break

    if now-1 >= 0 and visited[now-1] != True:
        root[now-1] = now
        visited[now-1] = True
        q.append([now-1, move+1])

    if now+1<100001 and visited[now+1] != True:
        root[now+1] = now
        visited[now+1] = True
        q.append([now+1, move+1])

    if now*2<100001 and visited[now*2] != True:
        root[now*2] = now
        visited[now*2] = True
        q.append([now*2, move+1])

result_root(n, k)