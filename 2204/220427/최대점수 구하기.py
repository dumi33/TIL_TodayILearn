def dfs(L,sum,time) :
    global ans
    if time > m : return # 시간제한 걸린경우
    if L == n : 
        if sum > ans :
            ans = sum
    else :
        dfs(L+1, sum+arr[L][0],time+arr[L][1]) # 해당 문제를 푼경우
        dfs(L+1, sum,time) # 문제를 안푼경우 
        
        
        
    
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    arr = []
    for i in range(n) :
        s,t = map(int,input().split())
        arr.append((s,t))
    ans = 0 #  최대 점수을 구하라 
    dfs(0,0,0)
    print(ans)
