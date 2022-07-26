def solution(n):
    answer = n
    n_bin = bin(n)[2:]
    n_num = n_bin.count("1")

    a_num = 0
    while n_num != a_num:
        answer += 1
        a_bin = bin(answer)[2:]
        a_num = a_bin.count("1")
    return answer