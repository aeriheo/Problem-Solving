ipt = int(input())
arr = [0] * 300
dp = []
for i in range(ipt):
    arr[i] = int(input())

dp.append(arr[0])
dp.append(max(arr[0]+arr[1], arr[1]))

if ipt>=3:
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3, ipt):
    dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1]))

print(dp[-1])
