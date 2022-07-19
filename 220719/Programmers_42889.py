def solution(N, stages):
    answer = []
    fail = []

    for idx in range(1, N + 1):
        now = 0
        person = 0
        for s in stages:
            if s == idx:
                now += 1
                person += 1
            if s > idx: person += 1

        if person != 0:
            fail.append([idx, now / person])
        else:
            fail.append([idx, 0])

    fail.sort(key=lambda x: -x[1])
    for f in fail:
        answer.append(f[0])
    return answer