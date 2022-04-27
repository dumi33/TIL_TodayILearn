def dfs(L,sum) :
    if L == k :
        if sum >0 : # 음수는 중복되므로 상관하지않는다.
            s.add(sum)
    else :
        dfs(L+1,sum+arr[L]) # 왼쪽에 놓는다.
        dfs(L+1,sum-arr[L]) # 오른쪽에 놓는다.
        dfs(L+1,sum) # 안놓는다. 
                    
if __name__=="__main__" :
    k = int(input())
    arr = list(map(int,input().split()))
    s = set() # 중복된 수를 자동으로 제거해준다.
    dfs(0,0)
    print(sum(arr)-len(s))
