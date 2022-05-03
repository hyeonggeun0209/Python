from sys import stdin
import sys
sys.setrecursionlimit(10000)

def cabbage(field,i,j,N,M):
    ex = 0
    position = [[0, 1], [1, 0],[-1, 0],[0, -1]]
    for px,py in position:
        nx = i + px
        ny = j + py
        if 0<= nx < N and 0 <= ny < M:
            if field[nx][ny] == 1:
                field[i][j] = 0
                cabbage(field,nx,ny,N,M)
            else : ex += 1
        else: ex += 1
    if ex == 4:
        field[i][j] = 0

T = int(stdin.readline())

for i in range(T):
    M,N,K = map(int, stdin.readline().split())
    field = [[0 for j in range(M)] for i in range(N)]
    count = 0
    for j in range(K):
        a,b = map(int, stdin.readline().split())
        field[b][a] = 1

    for n in range(N):
        for m in range(M):
            if field[n][m] == 1:
                cabbage(field,n,m,N,M)
                count += 1

    print(count)
