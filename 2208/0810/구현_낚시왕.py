# 상 하 우 좌 
dx = [-1,1,0,0]
dy = [0,0,1,-1]


# 상어 이동 
def move_shark() :
    new = [[[] for i in range(c)] for j in range(r)]
    for i in range(r) :
        for j in range(c) :
            if shark[i][j] :
                x,y = i,j
                s,d,z = shark[x][y][0]
                dist = s 
                while dist > 0 :
                    nx,ny = x + dx[d],y + dy[d]
                    # 벽과 충돌하지 않은 경우 
                    if 0<=nx<r and 0<=ny<c :
                        x,y = nx,ny 
                        dist -=1 
                    # 벽과 충돌한 경우 
                    else :
                        # 상 or 우 
                        if d == 0 or d == 2 :
                            d +=1 
                        elif d==1 or d == 3 :
                            d-=1 
                new[x][y].append([s,d,z])
    for i in range(r) :
        for j in range(c) :
            shark[i][j] = new[i][j]
            
            
            
# 상어 잡기  
def catch_shark() :
    global answer 
    
    # 낚시왕이 열을 돌아다니면서 
    for king in range(c) :
        # 땅과 가까운 곳을 확인 
        for x in range(r) :
            # 상어가 있다면 
            if shark[x][king] :
                s,d,z = shark[x][king].pop(0)
                answer+=z
                break 
            
        # 상어 움직이기 
        move_shark()
        
        # 한 곳에 상어가 여러마리 있는 경우 처리 
        for i in range(r) :
            for j in range(c) :
                # 상어가 2마리 이상 있는 경우 
                if len(shark[i][j])>1 :
                    shark[i][j].sort(key = lambda x : x[2], reverse = True)
                    while len(shark[i][j])>1 :
                        shark[i][j].pop()
                

if __name__=="__main__" :
    r,c,m = map(int,input().split())
    shark = [[[] for i in range(c)] for j in range(r)]
    for _ in range(m) :
        R,C,s,d,z = map(int,input().split())
        shark[R-1][C-1].append([s,d-1,z])
    
    answer = 0
    catch_shark()
    print(answer)
