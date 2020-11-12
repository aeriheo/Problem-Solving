n = int(input())
dp = [0,0]
if n>1:
    dp.append(1)
    dp.append(1)
for i in range(4, n+1):
    if i%6 == 0:
        dp.append(min(dp[int(i/2)]+1, dp[int(i/3)]+1, dp[i-1]+1))
    elif i%3 == 0:
        dp.append(min(dp[int(i/3)]+1, dp[i-1]+1))
    elif i%2 == 0:
        dp.append(min(dp[int(i/2)]+1, dp[i-1]+1))
    else:
        dp.append(dp[i-1]+1)

print(dp[-1])