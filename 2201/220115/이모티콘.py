from collections import deque

q = deque()
s = int(input())
dis = [[-1]*(s+1)for _ in range(s+1)]



def bfs() :
    q.append([1,0]) # 화면에 출력된 이모티콘의 개수, 클립보드의 이모티콘의 개수
    dis[1][0] = 0 

    while q:
        x,y = q.popleft()
        if  dis[x][x]==-1 :  # 1번연산 # 클립보드에 복사가 되어있지않다면?
            dis[x][x] = dis[x][y]+1
            q.append([x,x])
        if x+y <= s and dis[x+y][y]==-1: # 2번연산 # 클립보드에 있는 문자만큼 프린트
            dis[x+y][y]=dis[x][y]+1 # 할당하는 것을 ==로 적어서 1시간 넘게 헤맸다. 
            q.append([x+y,y])
        if x-1 >= 0 and dis[x-1][y]==-1: # 3번 연산 # 프린트 되어있는 임티 하나 제거
            dis[x-1][y]=dis[x][y]+1
            q.append([x-1,y])

bfs()
ans = -1
for i in range(s+1):
    if dis[s][i] != -1:
        if ans == -1 or ans > dis[s][i]:
            ans = dis[s][i]
print(ans)
