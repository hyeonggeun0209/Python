from sys import stdin

M, N = map(int, stdin.readline().split()) 
t_box=[0 for _ in range(N)]
for i in range(N):
    t_box[i]=list(map(int,stdin.readline().split()))
# print(t_box)

