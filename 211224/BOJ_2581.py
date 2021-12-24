import sys
def func(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num%i==0:
            return True
    return False

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
min_result = 10001
sum_result = 0
for i in range(M, N+1):
    if func(i)==False:
        sum_result += i
        if min_result>i:
            min_result = i
if sum_result==0:
    print(-1)
else:
    print(sum_result)
    print(min_result)