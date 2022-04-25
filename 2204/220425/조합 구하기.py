def dfs(L,front) :
    global ans
    if L == m :
        ans+=1
        for i in res :
            print(i, end= ' ')
        print()
    else : 
        for i in range(1,n+1) : 
            if i > front : # 선택한 숫자보다 큰 경우에만 진행한다. 
                res[L] = i
                dfs(L+1, i) # 선택한 숫자를 뒤에 넣는다. 
                 
if __name__=="__main__" :
    n,m = map(int,input().split())
    res = [0] * m
    ans = 0 
    dfs(0,0)
    print(ans)
