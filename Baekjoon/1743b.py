import queue
from sys import stdin

def garbage(field,i,j,N,M):
    count = 0
    queue = list([])
    queue.append([i,j])
    field[i][j] = 0
    position = [[0, 1], [1, 0],[-1, 0],[0, -1]]
    while queue:
        a = queue.pop()
        if  a:
            count += 1
        for px,py in position:
            nx = a[0]+ px
            ny = a[1] + py
            if 0<= nx < N and 0 <= ny < M:
                if field[nx][ny] == 1:
                    queue.append([nx,ny])
                    field[nx][ny] = 0
    return count

N,M,K = map(int, stdin.readline().split())
field = [[0 for j in range(M)] for i in range(N)]
for j in range(K):
    a,b = map(int, stdin.readline().split())
    field[a-1][b-1] = 1

# print(field)    
ans = 0
for n in range(N):
    for m in range(M):
        if field[n][m] == 1:
            ans = max(ans,garbage(field,n,m,N,M))

print(ans)