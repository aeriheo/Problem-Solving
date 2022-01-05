import sys
a, b = map(int, sys.stdin.readline().split())
max_value = 0
if a>b:
    for i in range(1, b+1):
        if a%i == 0 and b%i==0:
            if i > max_value :
                max_value = i
else:
    for i in range(1, a+1):
        if a%i == 0 and b%i==0:
            if i > max_value :
                max_value = i

a_value = int(a/max_value)
b_value = int(b/max_value)
result = max_value * a_value * b_value
print(max_value)
print(result)