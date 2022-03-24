from sys import stdin

N1,N2 = map(int,stdin.readline().split())
A1 = list(stdin.readline().strip())
A2 = list(stdin.readline().strip())
T = int(stdin.readline())
path = []

for i in range(1,N1+1) :
    path.append([A1[-i],'r','x'])
for i in range(N2) :
    path.append([A2[i],'l','x'])

temp = []
for i in range(T) :
    for k in range(len(path)):
        path[k][2] = 'x'
    for j in range(len(path)):
        if j+1 < len(path) and (path[j][1] == 'r') and (path[j+1][1] == 'l') and (path[j][2] == 'x') and (path[j+1][2] == 'x'):
            temp = path[j]
            path[j] = path[j+1]
            path[j][2] = 'o'
            path[j+1] = temp
            path[j+1][2] = 'o'
ans = []
for x,y,z in path:
    ans += x
print("".join(ans))