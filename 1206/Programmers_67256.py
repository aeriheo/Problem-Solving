def solution(numbers, hand):
    # 왼손은 * 에서 시작, 오른손은 #에서 시작
    # 왼손 1 4 7 *
    # 오른손 3 6 9 #
    # 거리가 같을 때 오른손 잡이면 오른손

    # key = 1, value = [4, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 5] 0 1 2 3 4 5 6 7 8 9 * # 순
    # * = 10 / # = 11로

    len_cnt = [0, 0]  # 왼쪽이 len_cnt[0] / 오른쪽이 len_cnt[1]
    left = 10
    right = 11
    dic = {0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1], 2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
           5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3], 8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2]}
    answer = ''

    for i in range(len(numbers)):
        print(left, right)
        if numbers[i] == 0 or numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8:
            tmp = dic.get(numbers[i])
            len_cnt[0] = tmp[left]
            len_cnt[1] = tmp[right]
            if len_cnt[0] < len_cnt[1]:
                answer += 'L'
                left = numbers[i]
            elif len_cnt[0] > len_cnt[1]:
                answer += 'R'
                right = numbers[i]
            elif len_cnt[0] == len_cnt[1]:
                if hand == "right":
                    answer += 'R'
                    right = numbers[i]
                else:
                    answer += 'L'
                    left = numbers[i]

        elif numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left = numbers[i]
            answer += 'L'

        else:
            right = numbers[i]
            answer += 'R'

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))