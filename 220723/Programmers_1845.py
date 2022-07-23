def solution(nums):
    answer = 0
    cnt = len(nums)//2
    s = len(set(nums))
    if cnt <= s:
        answer = cnt
    else:
        answer = s
    return answer