import sys
from collections import deque
input = sys.stdin.readline

def DFS(node):
    if node in graph.keys():
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                array_DFS.append(i)
                if i in graph.keys():
                    DFS(i)

def BFS(node):
    queue = deque([node])
    while queue:
        i = queue.popleft()
        if i in graph.keys():
            for j in graph[i]:
                if visited[j] == False:
                    visited[j] = True
                    array_BFS.append(j)
                    queue.append(j)

n, m, v = map(int, input().split())
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]

for k in graph.keys():
    graph[k].sort()

visited = [False] * (n+1)
visited[v] = True
array_DFS = [v]
DFS(v)

visited = [False] * (n+1)
visited[v] = True
array_BFS = [v]
BFS(v)

for data in array_DFS:
    print(data, end = ' ')
print()
for data in array_BFS:
    print(data, end = ' ')