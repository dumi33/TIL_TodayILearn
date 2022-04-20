def dfs(L,sum) :
    if sum > (total // 2) : # 절반보다  크면 
        return 
    if L == n:
        if sum == (total-sum) :
            print("YES")
            sys.exit(0)
    
    else :
        dfs(L+1, sum+array[L]) # 원소로 사용 
        dfs(L+1,sum) # 원소로 사용 X 
        
if __name__=="__main__" : 
    n = int(input())
    array = list(map(int,input().split()))
    total = sum(array)
    dfs(0,0)
    print("NO")
    
