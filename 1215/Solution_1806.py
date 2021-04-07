import sys
n, s = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
start = 0
end = 1
result = 100001
arr2 = [0] * (n+1)

for i in range(1, n+1):
    arr2[i] = arr[i-1] + arr2[i-1]

while start <= n-1 :
    arr_sum = arr2[end] - arr2[start]

    if arr_sum >= s :
        if result > end - start:
            result = end - start
        start += 1
    else:
        if end == n:
            start += 1
        else:
            end += 1

if result == 100001:
    print(0)
else:
    print(result)