def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = []
        temp = array[commands[i][0]-1:commands[i][1]]
        temp = sorted(temp)
        answer.append(temp[commands[i][2]-1])
    return answer


print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))