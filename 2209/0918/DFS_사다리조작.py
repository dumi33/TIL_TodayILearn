def check() :
    for i in range(1,n+1) :
        cur = i
        for j in range(1,h+1) :
            if mp[j][cur] : cur+=1 
            elif mp[j][cur-1] : cur-=1 
        if cur != i : return False 
    return True 

def dfs(idx,cnt) :
    global ans 
    if idx > 3 : return 
    if check() :
        ans = min(ans,idx)
        return 
    if idx == 3 :return 
    if idx  > ans : return 
    else :
        for added in range(cnt+1, len(candidate)) :
            i,j = candidate[added]
            if mp[i][j-1] == 0 and mp[i][j+1] == 0:
                    mp[i][j] = 1 
                    dfs(idx+1, added)
                    mp[i][j] = 0 
                    
        
if __name__=="__main__" :
    n,m,h = map(int,input().split())
    mp = [[0]*(n+1) for _ in range(h+1)]
    for i in range(m) :
        a,b = map(int,input().split())
        mp[a][b] = 1 
    ans = int(1e9)
    candidate = []
    for i in range(1,h+1) :
        for j in  range(1,n) :
            if mp[i][j] == 0 and mp[i][j-1] == 0 and mp[i][j+1] == 0:
                candidate.append([i,j]) 
    dfs(0,-1)
    
    if ans == int(1e9) : print(-1)
    else : print(ans)
