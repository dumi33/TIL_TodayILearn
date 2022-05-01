from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

    
if __name__=="__main__" :
    n = int(input())
    a = [list(map(int,input().split())) for i in range(n)]
    ch = [[0]*n for _ in range(n)]
    sum = 0
    q = deque()
    ch[n//2][n//2] = 1
    sum+=a[n//2][n//2]
    q.append((n//2,n//2))
    L = 0
    while True :
        if L==(n//2) : break 
        size = len(q)
        for i in range(size) :
            tmp = q.popleft()
            for j in range(4) :
                x = tmp[0]+dx[j]
                y = tmp[1]+dy[j]
                if 0<=x<n and 0<=y<n and ch[x][y]==0 :
                    ch[x][y] = 1
                    sum += a[x][y] 
                    q.append((x,y))
        L+=1 
    print(sum)
