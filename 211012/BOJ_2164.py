from collections import deque
n = int(input())
card = deque()
for i in range(1, n+1):
    card.append(i)

while len(card)!=1:
    card.popleft()
    t = card.popleft()
    card.append(t)

print(card[0])