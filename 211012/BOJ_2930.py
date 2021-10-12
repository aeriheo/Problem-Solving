round = int(input())
sanggeun = list(input())
other = int(input())
others = []
for _ in range(other):
    others.append(list(input()))

score = 0
max_score = 0
# score
for i in range(round):
    for j in range(other):
        if sanggeun[i] == 'S' and others[j][i] == 'P':
            score += 2
        elif sanggeun[i] == others[j][i]:
            score += 1
        elif sanggeun[i] == 'P' and others[j][i] == 'R':
            score += 2
        elif sanggeun[i] == 'R' and others[j][i] == 'S':
            score += 2

# max score
for i in range(round):
    lst = [0, 0, 0]
    for j in range(other):
        # S 경우
        if others[j][i] == 'P':
            lst[0] += 2
        elif others[j][i] == 'S':
            lst[0] += 1

        # P
        if others[j][i] == 'R':
            lst[1] += 2
        elif others[j][i] == 'P':
            lst[1] += 1

        # R
        if others[j][i] == 'S':
            lst[2] += 2
        elif others[j][i] == 'R':
            lst[2] += 1
    max_score += max(lst)

print(score)
print(max_score)