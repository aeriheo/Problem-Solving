import itertools, sys
n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
m_lst = list(map(int, sys.stdin.readline().split()))
math_lst = []
for i in range(len(m_lst)):
    for j in range(m_lst[i]):
        if i == 0:
            math_lst.append('+')
        elif i == 1:
            math_lst.append('-')
        elif i == 2:
            math_lst.append('*')
        elif i == 3:
            math_lst.append('/')
perm = set(itertools.permutations(math_lst, n-1))
result = []
perm = list(perm)
for i in perm:
    num = n_lst[0]
    for j in range(len(i)):
        if i[j] == '+':
            num += n_lst[j+1]
        elif i[j] == '-':
            num -= n_lst[j+1]
        elif i[j] == '*':
            num *= n_lst[j+1]
        elif i[j] == '/':
            if num < 0:
                num *= -1
                num /= n_lst[j+1]
                num = int(num)
                num *= -1
            else:
                num /= n_lst[j+1]
                num = int(num)
    result.append(num)

print(max(result))
print(min(result))