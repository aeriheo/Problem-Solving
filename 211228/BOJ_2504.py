from collections import deque
import sys
def func(lst):
    lst = deque(lst)
    temp = []
    start = lst.popleft()
    while lst:
        end = lst.popleft()
        if start == '(' and end == ')':
            temp.append(2)
            if len(lst) > 1:
                start = lst.popleft()
            elif len(lst) == 1:
                temp.append(lst.popleft())
                break
        elif start == '[' and end == ']':
            temp.append(3)
            if len(lst) > 1:
                start = lst.popleft()
            elif len(lst) == 1:
                temp.append(lst.popleft())
                break
        elif lst and end != ']' and end != ')' and end != '[' and end != '(':
            if start == '(' and lst[0] == ')':
                lst.popleft()
                end *= 2
                temp.append(end)
                if len(lst)>1:
                    start = lst.popleft()
                elif len(lst) == 1:
                    temp.append(lst.popleft())
                    break
            elif start == '[' and lst[0] == ']':
                lst.popleft()
                end *= 3
                temp.append(end)
                if len(lst) > 1:
                    start = lst.popleft()
                elif len(lst) == 1:
                    temp.append(lst.popleft())
                    break
            elif end != ']' and end != ')' and end != '[' and end != '(' and start != ']' and start != ')' and start != '[' and start != '(' :
                start = start + end
            else:
                temp.append(start)
                start = end
        elif len(lst) == 0 :
            temp.append(start)
            temp.append(end)
        else:
            temp.append(start)
            start = end
    return temp

v_lst = list(sys.stdin.readline().rstrip())
cnt = v_lst.count('[') + v_lst.count(']') + v_lst.count('(') + v_lst.count(')')
loop_cnt = 0
loop_len = len(v_lst)

while cnt > 0 and loop_cnt<loop_len :
    v_lst = func(v_lst)
    cnt = v_lst.count('[') + v_lst.count(']') + v_lst.count('(') + v_lst.count(')')
    loop_cnt += 1

if loop_cnt == loop_len:
    print(0)
else:
    print(sum(v_lst))