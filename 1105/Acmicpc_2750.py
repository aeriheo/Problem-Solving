def sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

n = int(input())
arr = []
for i in range(n):
    s = int(input())
    arr.append(s)

s_arr = sort(arr)
for ii in range(len(s_arr)):
    print(s_arr[ii])