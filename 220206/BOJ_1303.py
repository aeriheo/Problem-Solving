import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, c):
    global visited, w_result, b_result
    q = deque([[x, y]])
    cnt = 0
    while q:
        i, j = q.popleft()
        if visited[i][j] == True: continue
        visited[i][j] = True
        cnt += 1
        for k in range(4):
            xx = dx[k] + i
            yy = dy[k] + j
            if 0<=xx<m and 0<=yy<n :
                if visited[xx][yy] == False and field[xx][yy] == c:
                    q.append([xx, yy])
    cnt *= cnt
    if c == 'W': w_result += cnt
    else : b_result += cnt

n, m = map(int, input().split())
field = []
w_result = 0
b_result = 0
for _ in range(m):
    field.append(list(input().rstrip()))

visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j] == True: continue
        BFS(i, j, field[i][j])

print(w_result, b_result)