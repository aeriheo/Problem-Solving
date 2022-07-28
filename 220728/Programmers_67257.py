from itertools import permutations

pem = list(permutations(["+", "-", "*"], 3))

def solution(expression):
    answer = 0
    ex = []
    expression = list(expression)
    idx = 0
    for i in range(len(expression)):
        if expression[i] == "+" or expression[i] == "-" or expression[i] == "*":
            ex.append(int(''.join(expression[idx:i])))
            ex.append(expression[i])
            idx = i + 1
    ex.append(int(''.join(expression[idx:i + 1])))

    for p in pem:
        example = ex[:]
        for a in p:
            temp = []
            ex_len = len(example)
            i = 0
            while i < ex_len:
                if example[i] != a:
                    temp.append(example[i])
                    i += 1
                else:
                    x = temp.pop()
                    y = example[i + 1]
                    if a == "+":
                        temp.append(x + y)
                    elif a == "-":
                        temp.append(x - y)
                    else:
                        temp.append(x * y)
                    i += 2
            example = temp[:]
        answer = max(answer, abs(example[0]))

    return answer