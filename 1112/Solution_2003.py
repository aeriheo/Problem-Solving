num = input().split(" ")
N = int(num[0])
M = int(num[1])
arr = input().split(" ")
for i in range(N):
    arr[i] = int(arr[i])

cnt = 0
a = 0
b = 0
while a<=N-1 and b<=N-1:
    s = sum(arr[a:b+1])
    if s < M:
        b += 1
    elif s == M:
        cnt +=1
        a += 1
        b += 1
    else:
        a += 1
        b = a

print(cnt)