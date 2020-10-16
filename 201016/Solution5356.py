def func(arr):
    sol= ""
    l_max = [] # 각 행별 배열 길이
    for l in range(len(arr)):
        l_max.append(len(arr[l]))
    loop_max = max(l_max) # 최대 배열 길이만큼 loop
    for i in range(loop_max):
        if i < l_max[0]:
            sol += arr[0][i]
        else:
            pass
        if i < l_max[1]:
            sol += arr[1][i]
        else:
            pass
        if i < l_max[2]:
            sol += arr[2][i]
        else:
            pass
        if i < l_max[3]:
            sol += arr[3][i]
        else:
            pass
        if i < l_max[4]:
            sol += arr[4][i]
        else:
            pass
    return sol

T = int(input()) # test_case
for test_case in range(1, T+1):
    arr = []
    for i in range(5):
        s = input() # 2차원 배열로 입력
        arr.append(list(s))
    result = ""
    result = func(arr)
    print("#"+str(test_case), result)