from collections import deque

n, k = map(int, input().split())

data = [i for i in range(1, n+1)]
q = deque(data)
result = []
cnt = 1
while q:
    if cnt == k:
        cnt = 1
        result.append(q.popleft())
    else:
        cnt += 1
        p = q.popleft()
        q.append(p)

answer = '<'
for i in range(n-1):
    answer += str(result[i]) + ', '

answer += str(result[-1]) + '>'

print(answer)