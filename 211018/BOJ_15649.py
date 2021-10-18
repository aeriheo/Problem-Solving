import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
result = list(itertools.permutations(lst, m))
for i in result:
    for j in i:
        print(j, end=' ')
    print()