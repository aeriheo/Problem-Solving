import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
s_nums = {}

for k in set(nums):
    s_nums[k] = 0

for k in nums:
    s_nums[k] += 1

cnt = {}
for c in s_nums:
    k = s_nums[c]
    if k not in cnt.keys():
        cnt[k] = [c]
    else:
        cnt[k].append(c)

s = 0
for num in nums:
    s += num

keys = list(cnt.keys())
keys.sort(reverse=True)

print(round(s/n))
print(nums[n//2])
for k in keys:
    if len(cnt[k]) == 1:
        print(cnt[k][0])
        break
    cnt[k].sort()
    print(cnt[k][1])
    break
print(nums[-1]-nums[0])