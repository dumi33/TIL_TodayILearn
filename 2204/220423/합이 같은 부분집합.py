import sys

def dfs(L, sum) :
    if sum > total //2 :
        return 
    
    if  L == n :
        if sum == (total - sum) : 
            print("YES")
            sys.exit(0)

    else :
        dfs(L+1, arr[L] + sum)
        dfs(L+1, sum)
        
    
if __name__=="__main__" : 
    n = int(input())
    arr = list(map(int,input().split()))
    total = sum(arr)
    dfs(0, 0) 
    print("NO")
