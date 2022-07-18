from itertools import permutations

def solution(numbers):
    answer = 0
    nums = list(numbers)
    p = []
    for i in range(1, len(nums) + 1):
        temp = list(permutations(nums, i))
        p.extend(temp)

    perm = []
    p = list(set(p))

    for i in p:
        n = int(''.join(i))
        flag = 0
        if n == 1 or n == 0: continue
        for num in range(2, (n // 2) + 1):
            if n % num == 0:
                flag = -1
                break
        if flag == 0 and n not in perm: perm.append(n)
    answer = len(perm)
    return answer