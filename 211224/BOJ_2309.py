import sys, copy

def DFS(lst, n, r):
    if len(lst)==7:
        comb.append(lst)
        return
    for i in range(n, 9):
        visited[i] = True
        tmp = copy.deepcopy(lst)
        tmp.append(n_lst[i])
        DFS(tmp, i+1, r-1)
        visited[i] = False

n_lst = []
for _ in range(9):
    n_lst.append(int(sys.stdin.readline()))
visited = [False for _ in range(9)]
comb = []
DFS([], 0, 7)

result = []
for i in comb:
    sum_comb = 0
    for num in i:
        sum_comb += num
    if sum_comb == 100:
        result = i
        break

for i in range(len(result)):
    for j in range(i, len(result)):
        if result[i] > result[j]:
            temp = result[j]
            result[j] = result[i]
            result[i] = temp

for num in result:
    print(num)