import sys
input = sys.stdin.readline
h, m = map(int, input().split())
t = int(input())
if t>=60:
    a = int(t/60)
    b = t%60
    h += a
    m += b
else:
    m += t

if m>=60:
    h += 1
    m -= 60
if h>=24:
    h -= 24

print(h, m)