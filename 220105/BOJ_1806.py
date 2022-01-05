import sys
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
min_lenght = 100000001
start_index = 0
end_index = 1
value = [0]
for i in range(n):
    value.append(arr[i]+value[i])

while start_index < n+1 and end_index < n + 1 :
    if value[end_index] - value[start_index] >= s:
        if min_lenght > end_index - start_index:
            min_lenght = end_index - start_index
        start_index += 1
        end_index = start_index + 1
    else:
        end_index += 1
        if end_index == n + 1:
            start_index += 1
            end_index = start_index + 1
if min_lenght == 100000001:
    print(0)
else:
    print(min_lenght)