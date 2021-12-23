import sys
def func(num):
    result = False
    if num == 1:
        return True
    for i in range(2, num):
        if num%i==0:
            result = True
    return result

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in lst:
    if func(num)==False:
        cnt += 1
print(cnt)