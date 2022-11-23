from sys import stdin
from collections import deque
p = 0
case = int(stdin.readline())
for i in range(case):
    popq = deque()
    priorty = 0
    N, M = map(int,stdin.readline().split())
    dq = deque((list(map(int, stdin.readline().split()))))
    priorty,cnt,ans = 0, 0, 0
    M = dq[M]
    while(p < len(dq)):
        priorty = 0
        for k in range(len(dq)):
            if priorty < dq[k]:
                priorty = dq[k]
        #print(priorty)
        for j in range(len(dq)):
            a = dq[0]
            if priorty > a:
                dq.append(a)
                dq.popleft()
                print(dq)
            elif priorty == a:
                b = dq.popleft()
                popq.append(b)
                cnt += 1
                if b == M:
                    ans = cnt
#print(popq)
print(ans)