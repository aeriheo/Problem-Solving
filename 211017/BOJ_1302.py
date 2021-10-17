import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n):
    data = input().rstrip()
    if data in dic.keys():
        dic[data] += 1
    else:
        dic[data] = 1

result = []
for k, v in dic.items():
    result.append([k, v])

result.sort(key = lambda x : (-x[1], x[0]))
print(result[0][0])