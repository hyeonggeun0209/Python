from sys import stdin
def com(list,i,N):
    if i+list[i][0] > N or d[i] != 0:
        return
    elif i+list[i][0] == N:
        d[i] += list[i][1]
        return
    else:
        for j in range(i+list[i][0],N):
            if j+list[j][0] <= N:
                if(d[j] == 0) : com(list,j,N)
                d[i] = max(d[i],d[j])
        d[i] += list[i][1]

N = int(stdin.readline())
con = []
d = [0] * N
for i in range(N):
    con.append(list(map(int, stdin.readline().split())))
for i in range(N):
    com(con,i,N)
print(max(d))