result = 0
lst = []
for _ in range(7):
    num = int(input())
    if num%2==1:
        lst.append(num)
        result += num

if len(lst)==0:
    print(-1)
else:
    print(result)
    print(min(lst))