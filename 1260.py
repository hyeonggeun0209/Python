from sys import stdin
from collections import deque

# DFS구현
def dfs(v):
    visited_dfs[v] = 1                         # 방문처리
    print(v,end=' ')                         
    for i in range(n+1):
        if visited_dfs[i]==0 and graph[i][v]:  # 방문했었는지, 그리고 간선이 있는지 확인
            dfs(i)                                 # 재귀함수 호출

# BFS구현
def bfs(v):
    visited_bfs[v] = 1                         # 방문처리
    queue = deque()
    queue.append(v)                            # 큐에 노드 삽입
    while queue:                               # 큐에 노드가 없을때까지 반복
        node = queue.popleft()                 # 큐에서 빼주기
        print(node,end=' ')
        for i in range(n+1):
            if visited_bfs[i] == 0 and graph[i][node]: # 방문했었는지, 그리고 간선이 있는지 확인
                queue.append(i)                        # 큐에 노드 삽입
                visited_bfs[i] = 1                     # 방문처리

n,m,v = map(int,stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)] 

for i in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

visited_dfs = [0]*(n+1)
visited_bfs = [0] * (n+1)

dfs(v)
print()
bfs(v)
 