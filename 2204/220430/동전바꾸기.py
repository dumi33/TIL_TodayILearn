def dfs(L, sum) :
    global ans
    if sum > t : return 
    if L == k :
        if sum == t : ans+=1
    else :
        for i in range(arr[L][1]+1) : # 1부터 했어서 틀렸었다. 안들어가는 경우는 0이다. 
            dfs(L+1,sum+(arr[L][0]*i))           
    
            
if __name__=="__main__" :
    t = int(input())
    k = int(input())
    arr = []
    ans = 0
    for i in range(k) :
        a,b = map(int,input().split())
        arr.append((a,b))
    dfs(0,0)
    print(ans)
