import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    global result
    q = deque([[x, y]])
    cnt = 0
    while q:
        i, j = q.popleft()
        if visited[i][j] == True: continue
        visited[i][j] = True
        cnt += 1
        for m in range(4):
            xx = dx[m] + i
            yy = dy[m] + j
            if 0<=xx<r and 0<=yy<c and visited[xx][yy] == False and field[xx][yy] == 1:
                q.append([xx, yy])
    result = max(cnt, result)

r, c, k = map(int, input().split())
field = [[0] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
for _ in range(k):
    x, y = map(int, input().split())
    field[x-1][y-1] = 1

result = 0
for i in range(r):
    for j in range(c):
        if field[i][j] == 0 : continue
        if visited[i][j] == True : continue
        BFS(i, j)
print(result)