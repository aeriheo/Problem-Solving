import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
degree = [0 for _ in range(n)]
dic = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    degree[b-1] += 1
q = deque([i for i in range(1, n+1) if degree[i-1] == 0])
result = []
while q:
    person = q.popleft()
    result.append(person)
    for i in dic[person]:
        degree[i-1] -= 1
        if degree[i-1] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')
print()