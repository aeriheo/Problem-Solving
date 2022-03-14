import sys
input = sys.stdin.readline
data = []
n = int(input())
for i in range(666, 987654321):
    if len(data) == n: break
    if "666" in str(i):
        data.append(i)

print(data[n-1])