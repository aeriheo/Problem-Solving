import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, k = map(int, input().split())
result = 9876543210
cnt = 0
q = PriorityQueue()
q.put((0, n))
visited = [False] * 100001
while q:
    move, now = q.get()

    visited[now] = True

    if now == k :
        result = move
        break


    if now-1 >= 0 and visited[now-1] != True:
        q.put((move+1, now-1))
    if now+1<100001 and visited[now+1] != True:
        q.put((move+1, now+1))
    if now*2<100001 and visited[now*2] != True:
        q.put((move, now*2))


print(result)