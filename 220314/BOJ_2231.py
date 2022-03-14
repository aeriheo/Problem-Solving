import sys
input = sys.stdin.readline
data = [987654321] * 1000001

for i in range(1, 1000000):
    nums = list(str(i))
    num = i

    for j in nums:
        num += int(j)
    if num <= 1000000: data[num] = min(data[num], i)
    else: break

n = int(input())
if data[n] == 987654321: print(0)
else: print(data[n])