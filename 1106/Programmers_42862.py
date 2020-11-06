def solution(n, lost, reserve):
    answer = n - len(lost) # 현재 체육복을 가지고 온 학생
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer += 1
            reserve[reserve.index(lost[i])] = 0
            lost[i] = 0

    for i in range(len(lost)):
        if lost[i] == 0 :
            pass
        elif lost[i] - 1 in reserve and lost[i] - 1 != 0:
            answer += 1
            reserve[reserve.index(lost[i] - 1)] = 0
        elif lost[i] + 1 in reserve and lost[i] + 1 <= n:
            answer += 1
            reserve[reserve.index(lost[i] + 1)] = 0
    return answer

print(solution(3, [3], [1]))