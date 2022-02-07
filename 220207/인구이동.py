import sys
from collections import deque
input  = sys.stdin.readline
n,l,r = map(int,input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int,input().split()))) # []로 하면 안되고 list를 이용해 둘러싸야한다. 

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(i,j) :
    q = deque()
    temp = []
    q.append([i,j])
    temp.append([i,j])
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx,ny = dx[i]+x, dy[i]+y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==0 :
                if l <= abs(graph[x][y] - graph[nx][ny]) <=r : # 이 부분 까먹음 
                    visit[nx][ny] = 1   # 조건을 만족시켰다면 방문 
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp
cnt = 0
while True :
    visit = [[0]*n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n) :
            if visit[i][j] == 0 :
                visit[i][j] = 1 
                temp = bfs(i,j) # 연합된 영토 반환 
                if len(temp) > 1 :
                    isTrue = True
                    value =sum([graph[x][y] for x,y in temp]) // len(temp)
                    # 값을 구한 뒤 여기를 어떻게 하는지 모르겠음
                    for x,y in temp : # for문을 만들어 temp에서 x,y를 뽑아 모두 value값으로 설정 
                        graph[x][y] = value
    if not isTrue :
        break # while문을 벗어남 
    cnt+=1
print(cnt) 
