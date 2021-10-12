import sys

def Camel(data):
    result = [''.join(data[0])]
    for i in range(1, len(data)):
        d = list(data[i])
        result.append(d[0].upper())
        if len(d[1:])>0:
            result.append(''.join(d[1:]))
    return ''.join(result)

def Snake(data):
    result = []
    for i in data:
        result.append(''.join(i))
        result.append("_")
    result.pop()
    return ''.join(result)

def Pascal(data):
    result = []
    for i in data:
        d = list(i)
        result.append(d[0].upper())
        if len(d[1:])>0:
            result.append(''.join(d[1:]))
    return ''.join(result)

lst = list(sys.stdin.readline().split())
data = []
lst[0] = int(lst[0])
if lst[0] == 1:
    idx = 0
    for i in range(len(lst[1])):
        lst[1] = list(lst[1])
        if 'A'<=lst[1][i]<='Z':
            data.append(lst[1][idx:i])
            lst[1][i] = lst[1][i].lower()
            idx = i
    data.append(lst[1][idx:])

elif lst[0] == 2:
    lst[1] = ''.join(lst[1])
    data = lst[1].split('_')
else:
    idx = 0
    lst[1] = list(lst[1])
    lst[1][0] = lst[1][0].lower()
    for i in range(len(lst[1])):
        if 'A'<=lst[1][i]<='Z':
            data.append(lst[1][idx:i])
            lst[1][i] = lst[1][i].lower()
            idx = i
    data.append(lst[1][idx:])

print(Camel(data))
print(Snake(data))
print(Pascal(data))