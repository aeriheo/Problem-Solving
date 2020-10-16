def func(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    avg = float(sum/len(s))
    sol = 0

    for j in range(len(s)):
        if int(s[j])<=avg:
            sol += 1
    return sol

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    s = input().split(" ")
    result = func(s)
    print("#"+str(test_case), result)