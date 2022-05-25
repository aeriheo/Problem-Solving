# 부모노드 저장
p = []

# 부모노드 찾기
def find(u):
    if u != p[u]: p[u] = find(p[u])
    return p[u]

# 연결
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    # 부모노드 변경 
    p[max(root1, root2)] = min(root1, root2)

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])

    # 크루스칼 사용
    for i in range(n): p.append(i)

    edge = 0
    while 1:
        # edge 간선의 수
        if edge == n - 1: break
        u, v, wt = costs.pop(0)
        # 부모가 다르면 연결.
        if find(u) != find(v):
            union(u, v)
            answer += wt
            edge += 1

    return answer