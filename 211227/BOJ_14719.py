import sys
def sum_value(start, end):
    center_value = min(m_map[start], m_map[end])
    result = 0
    for idx in range(start+1, end):
        result += (center_value - m_map[idx])
    return result

h, w = map(int, sys.stdin.readline().split())
m_map = list(map(int, sys.stdin.readline().split()))
if m_map.count(0) == w-1:
    print(0)
else:
    start = 0
    end = start + 1
    result = 0
    while end <= len(m_map)-1:
        if m_map[start] > m_map[end]:
            if m_map[end] != max(m_map[start + 1:]):
                end += 1
            else:
                if end - start > 1:
                    result += sum_value(start, end)
                start = end
                end = start + 1
        else:
            if end - start > 1:
                result += sum_value(start, end)
            start = end
            end = start +1
    print(result)