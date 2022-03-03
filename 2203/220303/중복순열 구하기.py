def dfs(L) :
    global cnt
    if L == m :
        cnt+=1
        for i in ch :
            print(i,end= ' ')
        print()
    else :
        for i in range(1,n+1) :
            ch[L] = i
            dfs(L+1) 


if __name__ == "__main__" :
    n,m = map(int,input().split())
    ch = [0]*m
    cnt = 0
    dfs(0)
    print(cnt)
