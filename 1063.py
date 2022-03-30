from sys import stdin

def R(state,i):
    if state[i][0] == 'H':
        if i == 1:
            L(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]+1)
    if i == 0 and state[i] == state[i+1] :
        R(state,i+1)
    
def L(state,i):
    if state[i][0] == 'A':
        if i == 1:
            R(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]-1)
    if i == 0 and state[i] == state[i+1] :
        L(state,i+1)
def B(state,i):
    if state[i][1] == '1':
        if i == 1:
            T(state,i-1)
            return
        return
    else:
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]-1)
    if i == 0 and state[i] == state[i+1] :
        B(state,i+1)
def T(state,i):
    if state[i][1] == '8':
        if i == 1:
            B(state,i-1)
            return
        return
    else:
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]+1)
    if i == 0 and state[i] == state[i+1] :
        T(state,i+1)
def RT(state,i):
    if state[i][0] == 'H' or state[i][1] == '8':
        if i == 1:
            LB(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]+1)
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]+1)
    if i == 0 and state[i] == state[i+1] :
        RT(state,i+1)
def LT(state,i):
    if state[i][0] == 'A' or state[i][1] == '8':
        if i == 1:
            RB(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]-1)
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]+1)
    if i == 0 and state[i] == state[i+1] :
        LT(state,i+1)
def RB(state,i):
    if state[i][0] == 'H' or state[i][1] == '1':
        if i == 1:
            LT(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]+1)
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]-1)
    if i == 0 and state[i] == state[i+1] :
        RB(state,i+1)
def LB(state,i):
    if state[i][0] == 'A' or state[i][1] == '1':
        if i == 1:
            RT(state,i-1)
            return
        return
    else:
        state[i][0] = ord(state[i][0])
        state[i][0] = chr(state[i][0]-1)
        state[i][1] = ord(state[i][1])
        state[i][1] = chr(state[i][1]-1)
    if i == 0 and state[i] == state[i+1] :
        LB(state,i+1)
k,s,N= list(stdin.readline().split())
k_state = list(k)
s_state = list(s)
state = list([k_state] + [s_state])
N = int(N)
move = []
for i in range(N):
    move.append(stdin.readline().strip())
for j in range(N):
    globals()[move[j]](state,0)
print("".join(state[0]))
print("".join(state[1]))