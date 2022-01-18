import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * 100001
dp[0] = 1
result = 0
for _ in range(n):
    num = int(input())
    for i in range(num, k+1):
        dp[i] = dp[i] + dp[i-num]
print(dp[k])