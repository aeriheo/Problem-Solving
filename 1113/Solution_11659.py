import sys
n, m = map(int, input().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

s = [0] * n
s[0] = arr[0]

for i in range(1, n):
    s[i] = s[i-1] + arr[i]

for l in range(m):
    i, j = map(int, sys.stdin.readline().split(" "))
    if i!=1:
        print(s[j-1]-s[i-2])
    else:
        print(s[j-1])