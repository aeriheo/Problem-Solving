def func(place, inout, result, W, R, Wait):
    if inout>0:
        if 0 in place:
            i = place.index(0)
            place[i] = W[inout-1]
            result += R[i] * W[inout-1]
            # print("현재주차공간", place)

        else:
            Wait.append(inout)

            # print("현재주차공간", place)
            # print("대기 공간", Wait)
    else:
        inout *= -1
        j = place.index(W[inout-1])
        place[j] = 0
        if len(Wait) != 0:
            n = place.index(0)
            place[n] = W[Wait[0]-1]
            result += R[n] * W[Wait[0]-1]
            del Wait[0]

        # print("현재주차공간", place)
        # print("대기 공간", Wait)

    return place, result, Wait

T = int(input()) # test_case
for test_case in range(1, T+1):
    a = input().split(" ")
    n = int(a[0]) # 주차 공간 수
    m = int(a[1]) # 이용 차량 수
    R = []
    for i in range(n): # 공간 단위당 요금
        fee = int(input())
        R.append(fee)
    W = []
    for j in range(m): # 차량의 무게
        weight = int(input())
        W.append(weight)
    place = [0] * n
    result = 0
    Wait = []
    for p in range(2*m):
        inout = int(input())
        place, result, Wait = func(place, inout, result, W, R, Wait)
    print(result)