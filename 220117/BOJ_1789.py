import sys
input = sys.stdin.readline
s = int(input())
n_sum = 0
n = 0
number = 1
while n_sum < s:
    n_sum += number
    number += 1
    n += 1

if n_sum > s:
    for _ in range(2):
        number -= 1
        n_sum -= number
        n -= 1

    need = s - n_sum
    n += 1
print(n)