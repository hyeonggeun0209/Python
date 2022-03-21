from sys import stdin
import math
White = 0
Blue = 0
def confetti(Graph,N) :
    global White
    global Blue
    cntW,cntB = 0,0
    for i in range(len(Graph)):
        for j in range(len(Graph[i])):
            if Graph[i][j] == 0:
                cntW += 1
            elif Graph[i][j] == 1:
                cntB += 1
    if cntW == N*N:
        White+=1
        return 
    elif cntB == N*N:
        Blue+=1
        return     
    n = int(N/2)
    for i in range(0,len(Graph),n):
        for j in range(0,len(Graph),n):
            confetti([row[j:j+n] for row in Graph[i:i+n]],n)
        
     
N = int(stdin.readline())
if (1 <= math.log2(N)) and (math.log2(N) <= 7) :
    Graph = []
    for i in range(N):
        Graph.append(list(map(int, stdin.readline().split())))
    
    confetti(Graph,N)
    print(White,Blue)
