def solution(n):
    answer = 0
    i = 1
    while i*i<=n:
        if i*i == n:
            answer = (i+1)**2
            return answer
        else:
            i += 1
    answer = -1
    return answer

print(solution(121))