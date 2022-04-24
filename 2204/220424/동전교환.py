def dfs(L, sum) :
    global ans
    if L > ans : return 
    if sum > m : return 
    if sum == m :
        if L < ans :
            ans = L
    else : 
        for i in arr :
            dfs(L+1, sum + i)
        
if __name__=="__main__" :
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    ans = sys.maxsize
    arr.sort(reverse = True)
    dfs(0,0)
    print(ans)
