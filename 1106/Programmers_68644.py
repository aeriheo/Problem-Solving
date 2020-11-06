def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n = numbers[i] + numbers[j]
            if n not in answer:
                answer.append(n)
    answer = sorted(answer)
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))