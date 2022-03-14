import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
result = 0
n, m = map(int, input().split())
cards = list(map(int, input().split()))
q = deque(list(combinations(cards, 3)))

while q:
    data = q.popleft()
    if sum(data) > m: continue
    result = max(sum(data), result)

print(result)