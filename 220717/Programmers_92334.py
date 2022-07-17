def solution(id_list, report, k):
    answer = []
    dic = {}
    res = {}
    for id in id_list:
        dic[id] = []
        res[id] = 0

    for r in report:
        rep = r.split()
        if rep[0] not in dic[rep[1]]: dic[rep[1]].append(rep[0])

    for key in dic.keys():
        if len(dic[key]) >= k:
            for v in dic[key]: res[v] += 1

    for id in id_list:
        answer.append(res[id])
    return answer