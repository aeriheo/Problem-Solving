import sys

n = int(input()) #사진틀 개수
num = int(input()) # 추천 횟수
arr = list(map(int, sys.stdin.readline().split(" ")))
result = [] # 사진틀
result_cnt = [] # 사진 속 후보의 추천 횟수

for i in arr:
    if i in result:
        idx = result.index(i)
        result_cnt[idx] += 1
    elif len(result) <n:
        result.append(i)
        result_cnt.append(1)
    else:
        idx = result_cnt.index(min(result_cnt)) # 가장 작은 추천 수의 후보
        del result[idx]
        del result_cnt[idx]
        result.append(i)
        result_cnt.append(1)

result = sorted(result)
answer = ""
for j in result:
    answer += str(j)
    answer += " "
print(answer.rstrip())