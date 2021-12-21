import sys
now = 0
max_people = 0
for _ in range(10):
    out_, in_ = map(int, sys.stdin.readline().split())
    now -= out_
    now += in_
    if max_people < now:
        max_people = now
print(max_people)