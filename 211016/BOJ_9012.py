import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    left = 0
    right = 0
    lst = list(input().rstrip())
    if len(lst)%2 == 1:
        print("NO")
        continue
    # 0 True -1 False
    flag = 0
    for i in lst:
        # 시작이 닫는 부분일 때
        if left == 0 and right == 0 and i == ')':
            flag = -1
        elif i == '(':
            left += 1
        elif i == ')':
            right += 1
            # 닫는 갯수가 여는 갯수보다 많으면 안됨
            if left < right:
                flag = -1

    # 마지막이 여는 부분일 때
    if lst[-1] == "(":
        flag = -1
    # 여는 것과 닫는 것의 수는 같아야 한다.
    elif left != right:
        flag = -1

    if flag == 0:
        print("YES")
    else:
        print("NO")

