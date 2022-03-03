import sys
from collections import deque

input = sys.stdin.readline
N,L,R = map(int,input().split())
s =[] 
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(N) :
    s.append(list(map(int,input().split())))
def bfs(i,j) :
    q = deque()
    q.append([i,j])
    temp = []
    temp.append([i,j])
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny <N and visit[nx][ny] == 0 :
                if L<= abs(s[nx][ny]-s[x][y]) <= R :
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny]) # 연합한 영토들 
    return temp

cnt = 0
while True :
    visit = [[0] * N for i in range(N)]
    isTrue = False
    for i in range(N) :
        for j in range(N) :
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i,j)
                if len(temp) > 1 :
                    isTrue = True
                    num = sum([s[x][y] for x,y in temp]) // len(temp) # 연합한 영토의 값을 리스트를 만들어서 sum
                    for x,y in temp :
                        s[x][y] = num
    if not isTrue :
        break
    cnt+=1 # cnt 증가시킬 때마다 visit 다 리셋 
print(cnt)
