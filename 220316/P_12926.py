def solution(s, n):
    answer = ''
    lst = list(s)
    result = []
    for i in range(len(s)):
        if s[i] == " ":
            result.append(s[i])
            continue

        o = ord(s[i])
        o += n

        if (s[i].islower() and o > 122) or (s[i].isupper() and o > 90):
            o -= 26

        result.append(chr(o))

    answer = ''.join(result)
    return answer