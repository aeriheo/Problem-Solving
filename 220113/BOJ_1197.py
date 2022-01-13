import sys
input = sys.stdin.readline

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        root[rootB] = rootA
    else:
        root[rootA] = rootB

v, e = map(int, input().split())
edges = []
root = [0] * (v+1)
for idx in range(1, v+1):
    root[idx] = idx

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0

for edge in edges:
    c, a, b = edge
    if(find(a) != find(b)):
        union(a, b)
        result += c
print(result)
