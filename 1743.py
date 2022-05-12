from sys import stdin
import sys
sys.setrecursionlimit(10000)

def garbage(field,i,j,N,M,count):
    ex = 0
    count += 1
    position = [[0, 1], [1, 0],[-1, 0],[0, -1]]
    for px,py in position:
        nx = i + px
        ny = j + py
        if 0<= nx < N and 0 <= ny < M:
            if field[nx][ny] == 1:
                field[i][j] = 0
                count = garbage(field,nx,ny,N,M,count)
            else : ex += 1
        else: ex += 1
    if ex == 4:
        field[i][j] = 0
    return count

N,M,K = map(int, stdin.readline().split())
field = [[0 for j in range(M)] for i in range(N)]
for j in range(K):
    a,b = map(int, stdin.readline().split())
    field[a-1][b-1] = 1

#print(field)    
ans = 0
for n in range(N):
    for m in range(M):
        if field[n][m] == 1:
            count = 0
            ans = max(ans,garbage(field,n,m,N,M,count))

print(ans)