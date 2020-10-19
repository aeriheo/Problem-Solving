T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N 입력
    result = 1
    x = 1
    while result < N:
        x += 1
        result = x * x * x # x의 세제곱

    if result == N :
        print("#"+str(test_case), x)
    else :
        print("#"+str(test_case)+" -1")