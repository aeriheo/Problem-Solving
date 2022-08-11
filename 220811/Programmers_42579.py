def solution(genres, plays):
    answer = []
    dic = {}
    genre = {}
    for i in range(len(genres)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = [[i, plays[i]]]
            genre[genres[i]] = plays[i]
        else:
            dic[genres[i]].append([i, plays[i]])
            genre[genres[i]] += plays[i]

    temp = []
    for k in dic.keys():
        dic[k].sort(key=lambda x: (-x[1], x[0]))
        temp.append([k, genre[k]])

    temp.sort(key=lambda x: -x[1])

    for i in range(len(temp)):
        if len(dic[temp[i][0]]) < 2:
            answer.append(dic[temp[i][0]][0][0])
        else:
            answer.append(dic[temp[i][0]][0][0])
            answer.append(dic[temp[i][0]][1][0])
    return answer