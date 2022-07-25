def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while s != "1":
        # 0 제거
        s = list(s)
        s_zero = s.count("0")
        zero += s_zero

        # 길이 확인
        s_len = len(s) - s_zero
        s = bin(s_len)[2:]
        cnt += 1

    answer.append(cnt)
    answer.append(zero)

    return answer