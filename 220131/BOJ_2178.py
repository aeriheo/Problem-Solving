import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
m_map = []

for _ in range(n):
    m_map.append(list(input().rstrip()))

visited = [[False] * m for _ in range(n)]
q = deque([[0, 0, 1]])
visited[0][0] = True
result = 987654321

while q:
    i, j, v = q.popleft()
    if i == n-1 and j == m-1:
        print(v)
        break

    v += 1
    for idx in range(4):
        x = dx[idx] + i
        y = dy[idx] + j
        if 0<=x<n and 0<=y<m :
            if visited[x][y] == False and m_map[x][y] != '0':
                visited[x][y] = True
                q.append([x, y, v])
