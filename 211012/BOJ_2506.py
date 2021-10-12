import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

result = 0
cnt = 1
isCnt = False

for i in arr:
    if i == 1 and isCnt==False:
        result += cnt
        cnt += 1
        isCnt = True
    elif i==1 and isCnt == True:
        result += cnt
        cnt += 1
    elif i==0:
        isCnt = False
        cnt = 1

print(result)
