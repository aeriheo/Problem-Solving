import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [987654321] * 100001
dp[0] = 0
for _ in range(n):
    num = int(input())
    dp[num] = 1
    for i in range(num, k+1):
        dp[i] = min(dp[i], dp[i-num]+1)
if dp[k] == 987654321: dp[k] = -1
print(dp[k])