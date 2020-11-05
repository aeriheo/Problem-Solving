def func (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n >=2 :
        return func(n-1) + func(n-2)
    else:
        return func(0) + func(1)


print(func(int(input())))