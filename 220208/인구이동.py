from collections import deque 
import sys
input = sys.stdin.readline
n,l,r = map(int,input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int,input().split()))) # input뒤에 ()있다. 
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j) : # 연합된 마을 반환
    q = deque()
    temp = []
    q.append([i,j])
    temp.append([i,j])
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 :
                if l<=abs(graph[nx][ny] - graph[x][y]) <=r :
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp
cnt = 0
while True : 
    visit = [[0]*n for i in range(n)]
    isTrue = False
    for i in range(n) :
        for j in range(n) :
            if visit[i][j] == 0 :
                visit[i][j] = 1
                temp = bfs(i,j)
                if len(temp) > 1 : # 연합할 마을이 하나 이상일 때 
                    isTrue = True
                    value = sum([graph[x][y] for x,y in temp]) // len(temp) # sum 전에 리스트 형태로 만들어야 한다. 
                   
                    for x,y in temp :
                        graph[x][y] = value
    if isTrue == False : # 더이상 연합할 수 있는 마을이 없을 때 
        break
    cnt+=1 

print(cnt)
