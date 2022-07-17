from itertools import permutations

def solution(word):
    answer = 0
    lst = ['A', 'E', 'I', 'O', 'U'] * 5
    temp = []
    for i in range(1, 6):
        l = list(set(permutations(lst, i)))
        temp.extend(l)
    temp.sort()

    result = []
    for t in temp:
        result.append(''.join(t))

    answer = result.index(word) + 1
    return answer