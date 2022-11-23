from sys import stdin

N1,N2 = map(int,stdin.readline().split()) # N1,N2 입력 받기
A1 = list(stdin.readline().strip()) # 첫번째 개미열 입력 받기
A2 = list(stdin.readline().strip()) # 두번째 개미열 입력 받기
T = int(stdin.readline()) # 시간초 입력받기
path = [] # 전체 개미를 담을 리스트 준비

# 리스트에 개미들의 위치 입력, 첫번째 개미열은 역순으로 들어가야함
for i in range(1,N1+1) :
    path.append([A1[-i],'r','x'])
for i in range(N2) :
    path.append([A2[i],'l','x'])

# 시간초에 따른 개미들의 위치 전환
temp = []
for i in range(T) :
    for k in range(len(path)): # 1초가 지날때마다 개미들의 위치 변환 여부를 x으로 초기화
        path[k][2] = 'x'
    for j in range(len(path)):
        # j번째 개미가 마지막 개미가 아니여야함 and j번째 개미가 오른쪽으로 가고 그 다음 개미가 왼쪽으로 가야함 and
        # j번째 개미와 그 다음 개미가 모두 위치를 안바꾼 상태여야 함
        if j+1 < len(path) and (path[j][1] == 'r') and (path[j+1][1] == 'l') and (path[j][2] == 'x') and (path[j+1][2] == 'x'):
            temp = path[j]
            path[j] = path[j+1]
            path[j][2] = 'o'
            path[j+1] = temp
            path[j+1][2] = 'o'
# 개미들의 이름만 따로 저장해서 출력해주기            
ans = []
for x,y,z in path:
    ans += x
print("".join(ans))