import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m = map(int, input().split())
visited = [[False]*m for _ in range(n)]
value = [[0] * m for _ in range(n)]
result = 0
m_map = [list(map(int, input().split())) for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if m_map[i][j] == 1:
            q.append([i,j])
            visited[i][j] = True

while q:
    x, y = q.popleft()
    for i in range(8):
        xx = dx[i] + x
        yy = dy[i] + y
        if 0<=xx<n and 0<=yy<m and visited[xx][yy] == False:
            visited[xx][yy] = True
            value[xx][yy] = value[x][y] + 1
            result = max(result, value[xx][yy])
            q.append([xx, yy])

print(result)