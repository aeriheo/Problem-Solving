import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
dic = {}
for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0] * (n+1)
q = deque([1])
while q:
    c = q.popleft()
    if visited[c] == 1: continue
    visited[c] = 1
    for i in dic[c]:
        if visited[i] == 0 : q.append(i)

result = visited.count(1) -1
print(result)