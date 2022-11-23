import queue
from sys import stdin

# def garbage(field,i,j,N,M):
#     count = 0
#     queue = list([])
#     queue.append([i,j])
#     field[i][j] = 0
#     position = [[0, 1], [1, 0],[-1, 0],[0, -1]]
#     while queue:
#         if queue.pop() :
#             count += 1
#         for px,py in position:
#             nx = i + px
#             ny = j + py
#             if 0<= nx < N and 0 <= ny < M:
#                 if field[nx][ny] == 1:
#                     queue.append([nx,ny])
#     return count

N,M,K = map(int, stdin.readline().split())
field = [[0 for j in range(M)] for i in range(N)]
for j in range(K):
    a,b = map(int, stdin.readline().split())
    field[a-1][b-1] = 1
queue = list([])
queue.append([1,3])
print(queue.pop()[1])
# print(field)    
# ans = 0
# for n in range(N):
#     for m in range(M):
#         if field[n][m] == 1:
#             print(garbage(field,n,m,N,M))

# print(ans)