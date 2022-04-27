def dfs(L,sum) :
    global ans 
    if sum > t : return 
    if L == k :
        if sum == t :
            ans+=1
    else :
        for i in range(arr[L][1]+1) : # 동전이 개수만큼 돌린다. 
            dfs(L+1, sum+(arr[L][0]*i))
            
if __name__=="__main__" :
    t = int(input())
    k = int(input())
    arr = []
    for i in range(k) :
        cost, count = map(int,input().split())
        arr.append((cost,count))
    ans = 0
    dfs(0,0)
    print(ans)
