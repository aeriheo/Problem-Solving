def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        lst = []

        if n == 1:
            answer -= 1
            continue

        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                lst.append(i)
                lst.append(n // i)
        s = set(lst)
        if len(s) % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer