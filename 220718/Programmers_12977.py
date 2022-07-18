from itertools import combinations

def solution(nums):
    answer = 0

    comb = list(combinations(nums, 3))
    num = []
    for c in comb:
        num.append(sum(c))

    for n in num:
        flag = 0
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                flag = 1
                break
        if flag == 0: answer += 1
    return answer