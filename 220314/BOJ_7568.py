import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
res = []
res_cnt = {}
result = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j: continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    res.append([cnt, i])
    if cnt not in res_cnt.keys(): res_cnt[cnt] = 1
    else: res_cnt[cnt] += 1

for i in range(n):
    k = res[i][0]
    result[res[i][1]] = k+1


for r in result:
    print(r, end= ' ')