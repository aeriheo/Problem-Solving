import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(n):
    lst = list(sys.stdin.readline().rstrip())
    arr.append(lst)

# 방문을 했는가
visited = [[0] * m for _ in range(n)]

dx, dy = [-1,1,0,0],[0,0,-1,1]

result = 0

for i in range(len(arr[0])):
        if arr[0][i] == '0':
            visited[0][i] = 1
            queue = [(0, i)]
            while queue:
                x, y = queue.pop(0)

                if x== n-1 :
                    result = 1
                    break

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < n and 0 <= ny <m:
                        if visited[nx][ny] == 0 and arr[nx][ny] == '0':
                            visited[nx][ny]= 1
                            queue.append((nx,ny))

if result == 0:
    print("NO")
else:
    print("YES")