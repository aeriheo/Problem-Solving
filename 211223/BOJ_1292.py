import sys
a, b = map(int, sys.stdin.readline().split())
lst = []
num = 1
while len(lst)<=1000:
    for _ in range(num):
        lst.append(num)
    num += 1

result = 0
for i in range(a-1, b):
    result += lst[i]

print(result)