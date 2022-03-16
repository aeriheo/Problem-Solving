def solution(n):
    answer = 0

    # 3진법
    three = []
    while n >= 3:
        t = n % 3
        three.append(t)
        n = int(n / 3)
    three.append(n)

    # 10진법
    m = 1
    while three:
        t = three.pop()
        answer += (t * m)
        m *= 3

    return answer