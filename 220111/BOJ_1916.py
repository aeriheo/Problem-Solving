import sys
import heapq
def dijkstra(start):
    lst[start] = 0
    q = []
    heapq.heappush(q, [lst[start], start])

    while q:
        s_len, s = heapq.heappop(q)
        if lst[s] < s_len:
            continue
        for e, e_len in graph[s].items():
            d = s_len + e_len
            if d < lst[e]:
                lst[e] = d
                heapq.heappush(q, [d, e])

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {key : {} for key in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in graph[a].keys() and graph[a][b] > c:
        graph[a][b] = c
    elif b not in graph[a].keys():
        graph[a][b] = c
start, end = map(int, input().split())
lst = [987654321 for _ in range(n+1)]
dijkstra(start)
print(lst[end])