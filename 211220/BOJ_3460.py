import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    lst = []
    cnt = 0
    while n >= 1:
        if n%2 == 1:
            lst.append(str(cnt))
        n //= 2
        cnt += 1
    print(' '.join(lst))