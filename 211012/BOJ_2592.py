import sys
data = []
dic = {}
for _ in range(10):
    data.append(int(sys.stdin.readline().rstrip()))
    if data[-1] in dic.keys():
        dic[data[-1]] += 1
    else:
        dic[data[-1]] = 1

lst = []
for i in dic.keys():
    lst.append([i, dic[i]])

lst.sort(key = lambda x : -x[1])
print(sum(data)//10)
print(lst[0][0])
