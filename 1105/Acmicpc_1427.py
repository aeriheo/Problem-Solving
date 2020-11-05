s = input()
arr = list(s)

s_arr = sorted(arr, reverse=True)
result = ''.join(s_arr)
print(result)