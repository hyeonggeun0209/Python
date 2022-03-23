from sys import stdin
r,l,u,d = 0,0,0,0
row,col = 0,0
def num(list,i,j):
    global r
    global l
    global u
    global d
    global row
    global col
    r,l,u,d = 1,1,1,1
    if j+1 < len(list) and list[i][j] == list[i][j+1] :
        r += 1
        right(list,i,j+1)

    if i+1 < len(list) and list[i][j] == list[i+1][j] :
        d += 1
        down(list,i+1,j)
    
    if j-1 > -1 and list[i][j] == list[i][j-1] :
        l += 1
        left(list,i,j-1)

    if i-1 > -1 and list[i][j] == list[i-1][j] :
        u += 1
        up(list,i-1,j) 
    row = r+l-1
    col = u+d-1
    return max(row,col)
    
def right(list,i,j):
    global r
    if j+1 < len(list) and list[i][j] == list[i][j+1]:
        r += 1
        right(list,i,j+1)

def down(list,i,j):
    global d
    if i+1 < len(list) and list[i][j] == list[i+1][j]:
        d += 1
        down(list,i+1,j)

def left(list,i,j):
    global l
    if j-1 > -1 and list[i][j] == list[i][j-1]:
        l += 1
        left(list,i,j-1)

def up(list,i,j):
    global u
    if i-1 > -1 and list[i][j] == list[i-1][j]:
        u += 1
        up(list,i-1,j)

def switching(list,i,j,N,direction):
    arr = []
    if direction == 'r':
        temp = list[i][j]
        list[i][j] = list[i][j+1]
        list[i][j+1] = temp
        arr.append(num(list,i,j))
        arr.append(num(list,i,j+1))
        s_max = max(arr)
        list[i][j+1] = list[i][j]
        list[i][j] = temp
        return s_max
    elif direction == 'd':
        temp = list[i][j]
        list[i][j] = list[i+1][j]
        list[i+1][j] = temp
        arr.append(num(list,i,j))
        arr.append(num(list,i+1,j))
        s_max = max(arr)
        list[i+1][j] = list[i][j]
        list[i][j] = temp
        return s_max

N = int(stdin.readline())
candy = []
for i in range(N):
    candy.append(list(stdin.readline().strip()))

numarr = []
for i in range(N):
    for j in range(N):
        numarr.append(num(candy,i,j))

firstmax = max(numarr)
#print(firstmax)
for i in range(N):
    for j in range(N):
        if j+1 < len(candy) and candy[i][j] != candy[i][j+1] :
            a = switching(candy,i,j,N,'r')
            firstmax = max(firstmax,a)
        if i+1 < len(candy) and candy[i][j] != candy[i+1][j] :
            a = switching(candy,i,j,N,'d')
            firstmax = max(firstmax,a)
print(firstmax)
