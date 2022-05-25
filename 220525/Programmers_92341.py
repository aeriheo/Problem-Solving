def solution(fees, records):
    answer = []
    cars = {}
    for r in records:
        times, id, inout = r.split()
        if id not in cars.keys():
            cars[id] = [times]
        else:
            cars[id].append(times)

    cars_time = {}
    for c in cars.keys():
        cars_time[c] = 0
        lst = cars[c]
        if len(lst) % 2 == 1:
            lst.append("23:59")
        for i in range(0, len(lst), 2):
            h, m = lst[i].split(":")
            hh, mm = lst[i + 1].split(":")
            in_time = int(h) * 60 + int(m)
            out_time = int(hh) * 60 + int(mm)
            cars_time[c] += (out_time - in_time)

    result = []
    for ct in cars_time.keys():
        money = 0
        if cars_time[ct] < fees[0]:
            money = fees[1]
        else:
            money = fees[1]
            cars_time[ct] -= fees[0]
            if cars_time[ct] % fees[2] > 0:
                money += (cars_time[ct] // fees[2] + 1) * fees[3]
            else:
                money += (cars_time[ct] // fees[2]) * fees[3]
        result.append([ct, money])

    result.sort(key=lambda x: x[0])
    for r in result:
        answer.append(r[1])
    return answer