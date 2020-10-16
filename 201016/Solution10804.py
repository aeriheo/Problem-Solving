def func(s):
    arr = list(s)
    sol = ""
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == "b" : sol += "d"
        elif arr[i] == "d" : sol += "b"
        elif arr[i] == "p" : sol += "q"
        else: sol+="p"
    return sol

T = int(input()) # testcase
for i in range(T):
    s = input()
    result = func(s)
    print("#" + str(i+1), result)