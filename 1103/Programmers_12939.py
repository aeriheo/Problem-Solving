def solution(s):
    answer = ''
    arr = s.split(" ")
    a = []
    for i in range(len(arr)):
        a.append(int(arr[i]))
    a = sorted(a)
    answer = str(a[0]) + " " + str(a[-1])
    return answer

s = "-1 -2 -3 -4"
print(solution(s))